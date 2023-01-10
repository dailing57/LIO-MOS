import open3d as o3d
import numpy as np

global_path = 'data/global/'
local_path = 'data/local/'
res_path = 'data/res/'
pose_path = 'data/poses.txt'
tot = 3
D = 0.02

i = 0
for line in open(pose_path):
    if i >= tot:
        break
    ps = [float(it) for it in line.split()]
    gp = global_path + str(i).zfill(4) + '.pcd'
    lp = local_path + str(i).zfill(4) + '.pcd'
    res = res_path + str(i).zfill(4) + '.bin'
    i += 1
    T = np.eye(4)
    for j in range(12):
        T[int(j / 4)][j % 4] = ps[j]
    gpcd = o3d.io.read_point_cloud(gp)
    gpcd.transform(np.linalg.inv(T))
    pcd_tree = o3d.geometry.KDTreeFlann(gpcd)
    lpcd = o3d.io.read_point_cloud(lp)
    with open(res, 'wb') as f:
        for pt in lpcd.points:
            [k, idx, dis] = pcd_tree.search_knn_vector_3d(pt, 1)
            msk = 1 if dis[0] < D else 0
            f.write(msk.to_bytes(1, byteorder='little', signed=True))
    

