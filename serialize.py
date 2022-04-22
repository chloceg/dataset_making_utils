import os
import cv2
import numpy as np

if __name__ == '__main__':
    video_path = '/home/archer/Desktop/chapter4/videos/'
    frames_save_path = '/home/archer/Desktop/chapter4/frames/'


    def video_split(video, path):
        # videopath = video_path + video
        vs = cv2.VideoCapture(video)
        c = 1
        if vs.isOpened():
            # val, frame = vs.read()
            val = True
        else:
            val = False
        while val:
            val, frame = vs.read()
            # 每秒提取24帧图片
            if c % 3 == 0 and val == True:
                cv2.imwrite(path + "/" + str('%06d' % c) + '.jpg', frame)
                cv2.waitKey(0)
            c = c + 1
        vs.release()
        return 0


    # for parents, dirs, filenames in os.walk(video_path):
    #     # 对每视频数据进行遍历
    #     for file in filenames:
    #         file_name = file.split(".")[0]
    #         save_path_ = frames_save_path + "/" + file_name
    #         if not os.path.isdir(save_path_):
    #             os.makedirs(save_path_)
    #         # video_path = path + "/" + file
    #         print('here')
    #         video_split(video_path + '/' + file, save_path_)

    save_path = '/home/archer/Desktop/chapter4/frames/77/'
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    video_split('/home/archer/Desktop/chapter4/videos/7.mp4', save_path)
