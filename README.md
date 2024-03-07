# PSMNet
PSMNet，一个用于双目深度估计的项目，在KITTI数据集上训练和评估，可以产出视差图，深度图（灰度和RGB）

原项目地址https://github.com/JiaRenChang/PSMNet

原项目可以通过双目摄像头文件生成灰度视差图

test.m：调用disp_read.m和disp_to_color.m文件，将灰度视差图转变为彩色视差图，物体深度区别更明显

distance.py：利用视差图生成深度图，深度图的灰度值就是真实距离，单位毫米

mouse_gray.py：展示灰度图，输出鼠标停留的像素的灰度值

velodyne_vis.py：读取点云文件，生成点云。shift+鼠标左键可以输出该点在点云中的坐标
