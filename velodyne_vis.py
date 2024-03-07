import numpy as np
import struct
import open3d
import os
path = "F:/PSMNet/result_velodyne/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
def read_bin_velodyne(path):
    '''read bin file and transfer to array data'''
    pc_list=[]
    with open(path,'rb') as f:
        content=f.read()
        pc_iter=struct.iter_unpack('ffff',content)
        for idx,point in enumerate(pc_iter):
            pc_list.append([point[0],point[1],point[2]])
    return np.asarray(pc_list,dtype=np.float32)

def main():
    pc_path='F:/PSMNet/result_velodyne/000013.bin'
    # example=read_bin_velodyne(pc_path)
    example = np.fromfile(pc_path, dtype=np.float32, count=-1).reshape(-1, 4)
    example_xyz=example[:,:3]
    example_xyz=example_xyz[example_xyz[:,2]>-3]

    # From numpy to Open3D
    pcd = open3d.open3d.geometry.PointCloud()
    pcd.points= open3d.utility.Vector3dVector(example_xyz)
    vis_ = open3d.visualization.VisualizerWithEditing()
    vis_.create_window()
    vis_.add_geometry(pcd)
    render_options = vis_.get_render_option()
    render_options.point_size = 20
    render_options.background_color = np.array([0, 0, 0])
    #pcd.points= open3d.open3d.utility.Vector3dVector(example)
    #open3d.open3d.visualization.draw_geometries([pcd])
    vis_.run()
    #open3d.visualization.draw_geometries_with_editing([pcd])
    
    vis_.destroy_window()
   
if __name__=="__main__":
    main()

