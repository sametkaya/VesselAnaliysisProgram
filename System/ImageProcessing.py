from collections import deque

import bm4d as bm4d
import cv2
import numpy as np
import skimage
from skimage.morphology import disk
from skimage.util import img_as_float
from plantcv.plantcv import dilate
from plantcv.plantcv import params
from plantcv.plantcv import find_objects
from plantcv.plantcv import color_palette
from plantcv.plantcv import image_subtract
from plantcv.plantcv.morphology import find_branch_pts
from plantcv.plantcv._debug import _debug

from GraphicItems.VAP_Vein import VAP_Vein
from Model.VAP_Point import VAP_Point_Type, VAP_Point


def GetImageFormats(ImagePath):
    image_raw = cv2.imread(ImagePath)
    image_gray = cv2.cvtColor(image_raw, cv2.COLOR_BGR2GRAY)

    return image_raw, image_gray

def GetVascularAreaFractionValues(image_byte):
    pixelCount = image_byte.size
    whitePixelCount = np.sum(image_byte == 255)
    blackPixelCount = pixelCount-whitePixelCount
    ratio = (whitePixelCount * 100) /  pixelCount
    return ratio, whitePixelCount, blackPixelCount




def DenoiseImage(image_byte):
    image_fload = img_as_float(image_byte)
    imagef_bm4d = bm4d.bm4d(image_fload, sigma_psd=0.1)
    image_byte = ((imagef_bm4d - imagef_bm4d.min()) * (1 / (imagef_bm4d.max() - imagef_bm4d.min()) * 255)).astype('uint8')
    #cv2.imshow('bm4d', image_byte)
    #skimage.io.imsave("image_BM4D_byte.png", image_byte)
    return image_byte

def Segment(image_byte):
    image_float = skimage.filters.gaussian(image_byte, sigma=1)
    triangle_tresh = skimage.filters.threshold_triangle(image_float)
    triangle_uint8 = ((image_float > triangle_tresh) * 255).astype('uint8')
    #cv2.imshow('triangle_byte', triangle_uint8)
    #skimage.io.imsave("image_triangle_byte.png", triangle_uint8)
    return triangle_uint8

def BinaryClosing(image_byte):
    image_bool = 0 < image_byte
    footprint = disk(2)
    binary_closed_bool = skimage.morphology.binary_closing(image_bool, footprint)
    binary_closed_uint8 = (binary_closed_bool * 255).astype('uint8')
    #cv2.imshow('binary_closed_uint8', binary_closed_uint8)
    return binary_closed_uint8

def RemoveSmallObject(image_byte):
    image_bool = 0 < image_byte
    removed_image_bool = skimage.morphology.remove_small_objects(image_bool, 40)
    removed_image_uint8 = (removed_image_bool * 255).astype('uint8')
    #cv2.imshow('removed_image_uint8', removed_image_uint8)


    return removed_image_uint8

def Skeletonize(image_byte):
    image_bool = 0 < image_byte
    image_skel_bool = skimage.morphology.skeletonize(image_bool)
    image_skel_uint8 = (image_skel_bool * 255).astype('uint8')
    #cv2.imshow('skeleton_uint8', skeleton_uint8)
    skimage.io.imsave("image_skel_uint8.png", image_skel_uint8)
    image_skel_trans = np.zeros((image_skel_uint8.shape[1],image_skel_uint8.shape[0], 4), dtype=np.uint8)
    #image_skel_trans[:, :, :3] = image_skel_uint8[:, :, np.newaxis]
    image_skel_trans[:, :, 0] = 255
    image_skel_trans[:, :, 1] = 0
    image_skel_trans[:, :, 2] = 0
    image_skel_trans[:, :, 3] = image_skel_uint8
    #skimage.io.imsave("image_skel_trans.png", image_skel_trans)
    return image_skel_uint8

def find_branch_pts(image_skel_uint8):
    # In a kernel: 1 values line up with 255s, -1s line up with 0s, and 0s correspond to don't care
    # T like branch points
    t1 = np.array([[-1, 1, -1],
                   [1, 1, 1],
                   [-1, -1, -1]])
    t2 = np.array([[1, -1, 1],
                   [-1, 1, -1],
                   [1, -1, -1]])
    t3 = np.rot90(t1)
    t4 = np.rot90(t2)
    t5 = np.rot90(t3)
    t6 = np.rot90(t4)
    t7 = np.rot90(t5)
    t8 = np.rot90(t6)

    # Y like branch points
    y1 = np.array([[1, -1, 1],
                   [0, 1, 0],
                   [0, 1, 0]])
    y2 = np.array([[-1, 1, -1],
                   [1, 1, 0],
                   [-1, 0, 1]])
    y3 = np.rot90(y1)
    y4 = np.rot90(y2)
    y5 = np.rot90(y3)
    y6 = np.rot90(y4)
    y7 = np.rot90(y5)
    y8 = np.rot90(y6)
    kernels = [t1, t2, t3, t4, t5, t6, t7, t8, y1, y2, y3, y4, y5, y6, y7, y8]

    skel_img_padded = np.pad(image_skel_uint8, pad_width=1)

    #branch_pts_img = np.zeros(image_skel_uint8.shape[:2], dtype=int)
    branch_pts_img_padded = np.zeros(skel_img_padded.shape[:2], dtype=int)
    branch_pts_img = np.zeros(image_skel_uint8.shape[:2], dtype=int)

    # Store branch points
    for kernel in kernels:
        branch_pts_img_padded = np.logical_or(cv2.morphologyEx(skel_img_padded, op=cv2.MORPH_HITMISS, kernel=kernel,
                                                        borderType=cv2.BORDER_CONSTANT, borderValue=0), branch_pts_img_padded)
        branch_pts_img = np.logical_or(cv2.morphologyEx(image_skel_uint8, op=cv2.MORPH_HITMISS, kernel=kernel,
                                                        borderType=cv2.BORDER_CONSTANT, borderValue=0),
                                       branch_pts_img)

    # Switch type to uint8 rather than bool
    branch_pts_img_padded = branch_pts_img_padded.astype(np.uint8) * 255


    branch_objects, _ = find_objects(branch_pts_img_padded, branch_pts_img_padded)

    branch_list = []
    for i, branch in enumerate(branch_objects):
        x, y = branch.ravel()[:2]
        branch_list.append(VAP_Point(y-1, x-1, VAP_Point_Type.BRANCH))
    return branch_list
def find_tips(image_skel_uint8):

    # In a kernel: 1 values line up with 255s, -1s line up with 0s, and 0s correspond to dont care
    endpoint1 = np.array([[-1, -1, -1],
                          [-1,  1, -1],
                          [ 0,  1,  0]])
    endpoint2 = np.array([[-1, -1, -1],
                          [-1,  1,  0],
                          [-1,  0,  1]])

    endpoint3 = np.rot90(endpoint1)
    endpoint4 = np.rot90(endpoint2)
    endpoint5 = np.rot90(endpoint3)
    endpoint6 = np.rot90(endpoint4)
    endpoint7 = np.rot90(endpoint5)
    endpoint8 = np.rot90(endpoint6)

    endpoints = [endpoint1, endpoint2, endpoint3, endpoint4, endpoint5, endpoint6, endpoint7, endpoint8]
    skel_img_padded = np.pad(image_skel_uint8, pad_width=1)
    tip_img = np.zeros(skel_img_padded.shape[:2], dtype=int)
    #skel_img_padded = np.pad(skel_img, pad_width=1)
    for endpoint in endpoints:
        tip_img = np.logical_or(cv2.morphologyEx(skel_img_padded, op=cv2.MORPH_HITMISS, kernel=endpoint, borderType=cv2.BORDER_CONSTANT, borderValue=0), tip_img)
    #tip_img = np.delete(tip_img, 0, 0)
    #tip_img = np.delete(tip_img, 0, 1)
    #tip_img = np.delete(tip_img, tip_img.shape[0]-1, 0)
    #tip_img = np.delete(tip_img, tip_img.shape[1]-1, 1)
    tip_img = tip_img.astype(np.uint8) * 255


    tip_objects, _ = find_objects(tip_img, tip_img)

    tip_list= []
    for i, tip in enumerate(tip_objects):
        x, y = tip.ravel()[:2]
        tip_list.append(VAP_Point(y-1, x-1, VAP_Point_Type.TIP))

    return tip_list

def find_branch_pts2(image_skel_uint8):

    # T like branch points
    t1 = np.array([[-1, 1, -1],
                   [1, 1, 1],
                   [-1, -1, -1]])
    t2 = np.array([[1, -1, 1],
                   [-1, 1, -1],
                   [1, -1, -1]])
    t3 = np.rot90(t1)
    t4 = np.rot90(t2)
    t5 = np.rot90(t3)
    t6 = np.rot90(t4)
    t7 = np.rot90(t5)
    t8 = np.rot90(t6)

    # Y like branch points
    y1 = np.array([[1, -1, 1],
                   [0, 1, 0],
                   [0, 1, 0]])
    y2 = np.array([[-1, 1, -1],
                   [1, 1, 0],
                   [-1, 0, 1]])
    y3 = np.rot90(y1)
    y4 = np.rot90(y2)
    y5 = np.rot90(y3)
    y6 = np.rot90(y4)
    y7 = np.rot90(y5)
    y8 = np.rot90(y6)

    branch_points_kernels = [t1, t2, t3, t4, t5, t6, t7, t8, y1, y2, y3, y4, y5, y6, y7, y8]

    # In a kernel: 1 values line up with 255s, -1s line up with 0s, and 0s correspond to dont care
    endpoint1 = np.array([[-1, -1, -1],
                          [-1, 1, -1],
                          [0, 1, 0]])
    endpoint2 = np.array([[-1, -1, -1],
                          [-1, 1, 0],
                          [-1, 0, 1]])

    endpoint3 = np.rot90(endpoint1)
    endpoint4 = np.rot90(endpoint2)
    endpoint5 = np.rot90(endpoint3)
    endpoint6 = np.rot90(endpoint4)
    endpoint7 = np.rot90(endpoint5)
    endpoint8 = np.rot90(endpoint6)

    tip_points_kernels = [endpoint1, endpoint2, endpoint3, endpoint4, endpoint5, endpoint6, endpoint7, endpoint8]



    image_skel_padded = np.pad(image_skel_uint8, pad_width=1)

    branch_pts_img_padded = np.zeros(image_skel_padded.shape[:2], dtype=np.uint8)
    tip_pts_img_padded = np.zeros(image_skel_padded.shape[:2], dtype=np.uint8)

    # Store branch points
    for kernel in branch_points_kernels:
        branch_pts_img_padded = np.logical_or(cv2.morphologyEx(image_skel_padded, op=cv2.MORPH_HITMISS, kernel=kernel,borderType=cv2.BORDER_CONSTANT, borderValue=0), branch_pts_img_padded)

    pts_img_padded = branch_pts_img_padded.astype(np.uint8) * 2
    # Store tip points
    for kernel in tip_points_kernels:
        tip_pts_img_padded = np.logical_or(cv2.morphologyEx(image_skel_padded, op=cv2.MORPH_HITMISS, kernel=kernel,borderType=cv2.BORDER_CONSTANT, borderValue=0), tip_pts_img_padded)

    pts_img_padded = pts_img_padded + tip_pts_img_padded.astype(np.uint8)
    points = np.transpose(np.nonzero(pts_img_padded)) # take branch and tip points
    pts_img_padded = pts_img_padded + np.logical_or(image_skel_padded, image_skel_padded).astype(np.uint8)




    drawed_skel_img_padded = np.zeros(image_skel_padded.shape[:2], dtype=int)
    #All 8 directions
    #delta = [(-1, -1), (-1, 0), (-1, 1),
    #         (0, -1), (0, 1),
    #         (1, -1), (1, 0), (1, 1)]

    delta = [(-1, 0), (0, 1), (0, -1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    vap_vein_list = []
    id = 1
    for point in points:
        y, x = point

        if (drawed_skel_img_padded[y][x] == VAP_Point_Type.NONE.value):
            scan_veins_bfs = deque([])


            if (pts_img_padded[y][x] == VAP_Point_Type.BRANCH.value): # if branch point

                vap_branch_point = VAP_Point(y-1, x-1, VAP_Point_Type.BRANCH)
                #vap_vein.branch_points.append(vap_point)
                #drawed_skel_img_padded[y][x] = 3

                neigbors = []
                for dy, dx in delta:
                    yy, xx = y + dy, x + dx
                    # If the next position hasn't already been looked at and it's white
                    if pts_img_padded[yy][xx] > 0 and drawed_skel_img_padded[yy][xx] == 0:
                        #vap_vein = VAP_Vein()
                        scan_vein = VAP_Vein(id)
                        id = id + 1
                        vap_point = VAP_Point(yy - 1, xx - 1, pts_img_padded[yy][xx])
                        scan_vein.branch_points.append(vap_branch_point)
                        scan_vein.vap_point_list.append(vap_point)
                        drawed_skel_img_padded[yy][xx] = scan_vein.idn
                        scan_veins_bfs.append(scan_vein)

            elif (pts_img_padded[y][x] == VAP_Point_Type.TIP.value): # if tip point
                vap_point = VAP_Point(y-1, x-1, VAP_Point_Type.TIP)

                # vap_vein = VAP_Vein()
                scan_vein = VAP_Vein(id)
                id = id + 1
                scan_vein.vap_point_list.append(vap_point)
                scan_vein.tip_points.append(vap_point)
                scan_veins_bfs.append(scan_vein)

                drawed_skel_img_padded[y][x] = VAP_Point_Type.TIP.value
            else:
                vap_point = VAP_Point(y-1, x-1, VAP_Point_Type.PATH)
                # vap_vein = VAP_Vein()
                scan_vein = VAP_Vein(id)
                id = id + 1
                scan_vein.vap_point_list.append(vap_point)
                drawed_skel_img_padded[y][x] = scan_vein.idn
                scan_veins_bfs.append(scan_vein)



            while len(scan_veins_bfs) > 0:
                scan_vein = scan_veins_bfs.popleft()

                vap_point = scan_vein.vap_point_list[0]
                padded_point = VAP_Point(vap_point.y+1, vap_point.x+1, vap_point.vp_type)
                vap_point_bfs = deque([padded_point])
                #bfs = deque([VAP_Point(y, x, vap_point.vp_type)])

                while len(vap_point_bfs) > 0:
                    #p, t = bfs.popleft()
                    p = vap_point_bfs.popleft()
                    #y, x = p
                    hit_count = 0
                    hit_points= []
                    for dy, dx in delta: # directions
                        yy, xx = p.y + dy, p.x + dx

                        #next_vap_point = [[yy, xx], pts_img_padded[yy][xx]]
                        next_vap_point = VAP_Point(yy, xx, VAP_Point_Type(pts_img_padded[yy][xx]))
                        #if (yy == 26 and xx == 228):
                        #    print("break")
                        #if (pts_img_padded[yy][xx] > 0 and drawed_skel_img_padded[yy][xx] == 0 and next_vap_point not in vein.vap_point_list):
                        #if yy == 281 and xx == 443:
                        #    print("break")
                        if(pts_img_padded[yy][xx]>0 and drawed_skel_img_padded[yy][xx]==0 ):

                            if (pts_img_padded[yy][xx] == VAP_Point_Type.PATH.value):
                                #drawed_skel_img_padded[yy][xx] = VAP_Point_Type.PATH.value
                                drawed_skel_img_padded[yy][xx] = scan_vein.idn
                                vap_point = VAP_Point(yy-1, xx-1, VAP_Point_Type.PATH)
                                scan_vein.vap_point_list.append(vap_point)
                                vap_point_bfs.append(next_vap_point)
                                break
                            elif(pts_img_padded[yy][xx] == VAP_Point_Type.TIP.value):
                                drawed_skel_img_padded[yy][xx] = VAP_Point_Type.TIP.value
                                vap_point = VAP_Point(yy-1, xx-1, VAP_Point_Type.TIP)
                                if (vap_point in scan_vein.tip_points):
                                    continue
                                scan_vein.tip_points.append(vap_point)
                                scan_vein.vap_point_list.append(vap_point)
                                break
                            elif (pts_img_padded[yy][xx] == VAP_Point_Type.BRANCH.value):

                                vap_point = VAP_Point(yy-1, xx-1, VAP_Point_Type.BRANCH)
                                if (vap_point in scan_vein.branch_points and len(scan_vein.vap_point_list) < 2):
                                    continue
                                scan_vein.branch_points.append(vap_point)
                                #vap_vein.vap_point_list.append(vap_point)
                                break

                scan_vein.Build_Up()
                if (len(scan_vein.vap_point_list) > 1) or (len(scan_vein.branch_points) > 1):
                    scan_vein.idn = len(vap_vein_list) + 1
                    vap_vein_list.append(scan_vein)
                #else:
                #    for vap_point in scan_vein.vap_point_list:
                #        image_skel_uint8[vap_point.y][vap_point.x] = 0

    #return vap_vein_list, image_skel_uint8
    return vap_vein_list


def segment_skeleton(img_skel_uint8):

    # Store debug
    debug = params.debug
    params.debug = None

    # Find branch points
    _, bp = find_branch_pts(img_skel_uint8)

    bp = dilate(bp, 3, 1)

    # Subtract from the skeleton so that leaves are no longer connected
    segments = image_subtract(img_skel_uint8, bp)

    # Gather contours of leaves
    segment_objects, _ = find_objects(segments, segments)

    # Reset debug mode
    params.debug = debug
    return segment_objects

def find_all_branch_paths(img_skel_uint8):
    skel_img_padded = np.pad(img_skel_uint8, pad_width=1)

    branch_list = segment_skeleton(img_skel_uint8)
    branch_paths = []

    height, width = img_skel_uint8.shape

    #skel_img_padded = np.pad(img_skel_uint8, pad_width=1)

    # All 8 directions
    # delta = [(-1, -1), (-1, 0), (-1, 1),
    #          (0, -1),           (0, 1),
    #          (1, -1),   (1, 0), (1, 1)]
    delta = [(-1, -1),  (-1, 1), (1, -1),  (1, 1), (-1, 0), (0, -1), (0, 1), (1, 0)]
    index = 0

    for branch in branch_list:
        path_points = branch.reshape(-1, 2)
        mid = 0
        s = path_points[1:-1]
        for idx, x in enumerate(path_points[1:-1]):
            idx = idx+1
            pidx= idx-1
            nidx= idx+1
            if (path_points[pidx][0] == path_points[nidx][0] and path_points[pidx][1] == path_points[nidx][1]):
                mid = idx


        #mid = int((path_points.shape[0] + 1) / 2) + 1
        #if index==153:
        #    print("break")

        #print(index)
        path_points = path_points[mid:]

        for tip_no in [0,1]:
            start_point_padded = []
            prev_point = [-1, -1]
            if tip_no == 0: # start tip
                start_point_padded = path_points[0]+1

                if len(path_points)==1:
                    prev_point = path_points[0]+1
                else:
                    prev_point = path_points[1] + 1
            else: # end tip
                start_point_padded = path_points[-1] + 1
                if len(path_points) == 1:
                    prev_point = path_points[-2] + 1
                else:
                    prev_point = path_points[-2] + 1


            bfs = deque([start_point_padded])

            while len(bfs) > 0:
                x, y = bfs.popleft()
                # print(y,x)

                # Look all 8 directions for a good path
                hit_count = 0
                next_yx = np.array([[x, y]])-1
                hit_points = []
                for dy, dx in delta:
                    yy, xx = y + dy, x + dx
                    # If the next position hasn't already been looked at and it's white
                    if not (xx == prev_point[0] and yy == prev_point[1]) and skel_img_padded[yy][xx] > 0:
                        hit_count += 1
                        next_yx = np.array([[xx, yy]])-1
                        hit_points.append(next_yx)
                # 0 hit means line end without branch point
                # 2 or more hit means line end with branch point
                if hit_count == 1:
                    bfs.append(next_yx[0]+1)
                    if tip_no == 0:
                        prev_point = path_points[0]+1
                        path_points = np.insert(path_points, 0, next_yx, axis=0)
                    else:
                        prev_point = path_points[-1]+1
                        path_points = np.append(path_points, next_yx, axis=0)
                elif hit_count > 1:
                    if len(path_points) == 1: # sadece tek point için
                        prev_point = path_points[0] + 1
                        path_points = np.append(path_points, hit_points[1], axis=0)
                        path_points = np.insert(path_points,0 , hit_points[0], axis=0)
                    break
                else:
                    # skel_img_padded[prev_point[0]][prev_point[1]] = 0
                    break
        print(type(path_points[0]))
        lenght = float(cv2.arcLength(path_points, False))
        # 0 index, 1 lenght, 2 start, 3 end, 4 mid, 5 points
        branch_paths.append([index, lenght, path_points[0], path_points[-1], path_points[int(len(path_points)/2)], path_points])
        #branch_paths.append([index, lenght, path_points[0], path_points[-1], path_points])

        index += 1

    return branch_paths


if __name__ == "__main__":
    image_raw, image_byte8 = GetImageFormats(r"C:\Users\skaya\PycharmProjects\VesselAnaliysisProgram\Images\iskelet.png")
    find_branch_pts2(image_byte8)
    #find_all_branch_paths(image_byte8)