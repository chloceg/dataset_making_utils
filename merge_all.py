import os

imgpath = '/home/archer/Desktop/chapter4/frames/hy7/img'
rawpath = '/home/archer/Desktop/chapter4/frames/7/'

imgs = os.listdir(imgpath)
raw = os.listdir(rawpath)
imgs.sort()
raw.sort()

# 将图片的开始和结尾放入img文件夹中
for i in range(0, len(imgs), 2):
    begin = imgs[i].split('.')[0]
    end = imgs[i + 1].split('.')[0]
    # rawname = raw[i // 2].split('.')[0]
    for raw in range(int(begin), int(end)):
        os.system('cp ' + rawpath + '%06d' % int(raw) + '.jpg' + ' ' + imgpath)
