import numpy as np
import cv2


def video_detect():

    cap = cv2.VideoCapture('/home/archer/Desktop/chapter4/videos/小坑槽.mp4')
    video_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))    # 17

    four = cv2.VideoWriter_fourcc(*"mp4v")

    frame_count = 0

    while frame_count < video_num:

        frame_count = frame_count + 1
        success, img = cap.read()    # (960, 544, 3)
        if not success:
            continue
        print(img.shape)

        # cv2.namedWindow("Image")
        # cv2.imshow("Image", final_img)
        # cv2.waitKey(0)

        cv2.imwrite("小坑槽/" + str(frame_count).zfill(5) + '.jpg', img)

    cap.release()


video_detect()

