import open3d as o3d
import numpy as np
import os

lpcd = o3d.io.read_point_cloud('data/local/0001.pcd')
binfile = 'data/res/0001.bin'
with open(binfile, 'rb') as f:
    tot = os.path.getsize(binfile)
    np_color = np.ndarray((tot, 3))
    for i in range(tot):
        np_color[i,:] = [int.from_bytes(f.read(1), byteorder='little'),0,1]

lpcd.colors = o3d.utility.Vector3dVector(np_color)
o3d.visualization.draw_geometries([lpcd])