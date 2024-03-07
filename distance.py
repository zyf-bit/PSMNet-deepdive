import cv2
import numpy as np
import os
path = "F:/PSMNet/result_gray" #文件夹目录
pt="F:/PSMNet/result_distance"
files= os.listdir(path) #得到文件夹下的所有文件名称
fx = 4
baseline = 540

if __name__ == "__main__":
    for file in files:
        img = cv2.imread(path+"/"+file,-1)
        #print(img.dtype)
        print(file)

        depth = np.zeros_like(img, dtype=np.uint16)  # 深度图

        # 视差图转深度图
        for row in range(depth.shape[0]):
            for col in range(depth.shape[1]):
                d = img[row, col]

                if d == 0:
                    continue

                depth[row, col] = 256*256*fx * baseline / d

    #cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    #cv2.namedWindow("depth", cv2.WINDOW_NORMAL)
    #cv2.imshow("img", img)
    #cv2.imshow("depth", depth)
    #cv2.waitKey(0)
    #print(depth)
        cv2.imwrite(pt+"/"+file,depth)