import os


imgpath = '/home/archer/Desktop/chapter4/frames/hy6/img'
labelpath = '/home/archer/Desktop/chapter4/frames/hy6/label/'
imgs = os.listdir(imgpath)
labels = os.listdir(labelpath)
imgs.sort()
labels.sort()

for i in range(len(labels)):
    if imgs[i].split('.')[0] != labels[i].split('.')[0]:
        print(imgs[i], labels[i])
