import os

imgpath = '/home/archer/Desktop/chapter4/frames/hy7/img'
labelpath = '/home/archer/Desktop/chapter4/frames/hy7/label/'

imgs = os.listdir(imgpath)
labels = os.listdir(labelpath)
imgs.sort()
labels.sort()
# 将图片的开始和结尾放入img文件夹中
for i in range(0, len(imgs), 2):
    begin = imgs[i].split('.')[0]
    end = imgs[i + 1].split('.')[0]
    labelname = labels[i // 2].split('.')[0]
    for label in range(int(begin), int(end)+1):
        if int(begin) <= label <= int(end):
            # label += 1
            os.system('cp ' + labelpath + labelname + '.png' + ' ' + labelpath + '%06d' % int(label) + '.png')
