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

def DenoiseImage(ImagePath):
    image = cv2.imread(ImagePath, 0)
    image_fload = img_as_float(image)
    imagef_bm4d = bm4d.bm4d(image_fload, sigma_psd=0.1)
    image_byte = ((imagef_bm4d - imagef_bm4d.min()) * (1 / (imagef_bm4d.max() - imagef_bm4d.min()) * 255)).astype('uint8')
    #cv2.imshow('bm4d', image_byte)
    return image_byte

def Segment(image_byte):
    image_float = skimage.filters.gaussian(image_byte, sigma=1)
    triangle_tresh = skimage.filters.threshold_triangle(image_float)
    triangle_uint8 = ((image_float > triangle_tresh) * 255).astype('uint8')
    #cv2.imshow('triangle_byte', triangle_uint8)
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
    branch_pts_img = branch_pts_img.astype(np.uint8) * 255

    branch_objects, _ = find_objects(branch_pts_img_padded, branch_pts_img_padded)

    # Initialize list of tip data points
    #branch_list = []
    # All 8 directions
    delta = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]
    branch_labels = []
    branch_dict = {}
    for i, branch in enumerate(branch_objects):
        x, y = branch.ravel()[:2]
        coord = [int(y)-1, int(x)-1]
        #coord = [int(y), int(x) ]
        #branch_list.append(coord)
        branch_labels.append(i)
        neigbors = []
        for dy, dx in delta:
            yy, xx = y + dy, x + dx
            # If the next position hasn't already been looked at and it's white
            if skel_img_padded[yy][xx] > 0:
                neigbors.append([yy, xx])
        branch_dict[i] = [coord, neigbors]
        #branch_dict[i] = coord

    return branch_dict, branch_pts_img
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
    tip_img = np.delete(tip_img, 0, 0)
    tip_img = np.delete(tip_img, 0, 1)
    tip_img = np.delete(tip_img, tip_img.shape[0]-1, 0)
    tip_img = np.delete(tip_img, tip_img.shape[1]-1, 1)
    tip_img = tip_img.astype(np.uint8) * 255


    tip_objects, _ = find_objects(tip_img, tip_img)
    # All 8 directions
    delta = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]
    tip_dict = {}
    for i, tip in enumerate(tip_objects):
        x, y = tip.ravel()[:2]
        coord = [int(y), int(x)]
        neigbors = []
        for dy, dx in delta:
            yy, xx = y + dy, x + dx
            # If the next position hasn't already been looked at and it's white
            if skel_img_padded[yy][xx] > 0:
                neigbors.append([yy, xx])
        #tip_dict[i] = [coord, neigbors]
        tip_dict[i] = coord



    return tip_dict

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
        if index==131:
            print("break")

        print(index)
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
                    if len(path_points)==1: # sadece tek point için
                        prev_point = path_points[0] + 1
                        path_points = np.append(path_points, hit_points[1], axis=0)
                        path_points = np.insert(path_points,0 , hit_points[0], axis=0)
                    # if tip_no == 0:
                    #     path_points = np.insert(path_points, 0, next_yx, axis=0)
                    # else:
                    #     path_points = np.append(path_points, next_yx, axis=0)

                    # skel_img_padded[prev_point[0]][prev_point[1]] = 0
                    # prev_point = path_points[-1]
                    # skel_img_padded[prev_point[0]][prev_point[1]] = 0
                    break
                else:
                    # skel_img_padded[prev_point[0]][prev_point[1]] = 0
                    break
        lenght = float(cv2.arcLength(path_points, False))
        # 0 index, 1 lenght, 2 start, 3 end, 4 mid, 5 points
        branch_paths.append([index, lenght, path_points[0], path_points[-1], path_points[int(len(path_points)/2)], path_points])
        #branch_paths.append([index, lenght, path_points[0], path_points[-1], path_points])

        index += 1

    return branch_paths


