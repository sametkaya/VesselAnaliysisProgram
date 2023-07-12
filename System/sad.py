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
        lenght = float(cv2.arcLength(path_points, False))
        # 0 index, 1 lenght, 2 start, 3 end, 4 mid, 5 points
        branch_paths.append([index, lenght, path_points[0], path_points[-1], path_points[int(len(path_points)/2)], path_points])
        #branch_paths.append([index, lenght, path_points[0], path_points[-1], path_points])

        index += 1

    return branch_paths