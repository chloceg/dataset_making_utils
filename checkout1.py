# coding=utf-8
import time
import os
import cv2
import numpy as np
from PIL import Image


# 训练使用的txt标注是否正确
if __name__ == "__main__":
    filename = '/home/archer/Desktop/chapter4/frames/hy7/'
    file = os.listdir(filename + 'img/')
    file.sort()

    for name in file:
        obj = name.split('.')
        img_path = filename + 'img/' + obj[0] + '.jpg'
        label_path = filename + 'label/' + obj[0] + '.png'

        # print(img_path)
        # print(label_path)

        # 这里Image读取到的居然是三通道矩阵，取第一个通道作为标签即可
        img = cv2.imread(img_path)
        label = np.array(Image.open(label_path))
        # print(label)
        # print(img.shape, label.shape)

        # test文件夹中Image读取到的居然是三通道矩阵，取第一个通道作为标签即可。
        # 而train文件夹中Image读取到的却是单通道矩阵，直接取索引。

        index = (label == 1)
        img[index] = [0, 0, 255]

        cv2.namedWindow("img")
        cv2.imshow("img", cv2.resize(img, (1280, 720)))
        cv2.waitKey(1)



