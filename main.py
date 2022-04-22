import os


# 融合json2dataset+copypngfromjson
jsonpngpath = '/home/archer/Desktop/chapter4/frames/hy77/label_json/'
labelpath = '/home/archer/Desktop/chapter4/frames/hy77/label_temp/'
labelsavepath = '/home/archer/Desktop/chapter4/frames/hy77/label/'
imgpath = '/home/archer/Desktop/chapter4/frames/hy77/img_temp/'
imgsavepath = '/home/archer/Desktop/chapter4/frames/hy77/img/'
rawpath = '/home/archer/Desktop/chapter4/frames/77/'


def jsontodataset(labelpath, jsonpngpath):
    json = os.listdir(jsonpngpath)
    json.sort()
    for i in json:
        if i.endswith('_json'): continue
        os.system('labelme_json_to_dataset ' + jsonpngpath + i)

    jsons = os.listdir(jsonpngpath)
    jsons.sort()

    for i in jsons:
        if i.endswith('_json'):
            n = i.split('_')[0]
            os.system('cp ' + jsonpngpath + i + '/label.png' + ' ' + labelpath + n + '.png')


jsontodataset(labelpath, jsonpngpath)


def labelcopy(imgpath, labelpath, labelsavepath, rawpath):
    # 融合copypng+mergeall
    imgs = os.listdir(imgpath)
    labels = os.listdir(labelpath)
    imgs.sort()
    labels.sort()
    # 将图片的开始和结尾放入img文件夹中
    for i in range(0, len(imgs), 2):
        begin = imgs[i].split('.')[0]
        end = imgs[i + 1].split('.')[0]
        print(begin, end)

        labelname = labels[int(i / 2)].split('.')[0]
        for label in range(int(begin), int(end)+1):
            if os.path.exists(rawpath + '%06d' % label + '.jpg'):
                os.system('cp ' + labelpath + labelname + '.png' + ' ' + labelsavepath + '%06d' % label + '.png')


labelcopy(imgpath, labelpath, labelsavepath, rawpath)


def mergeimg(imgpath, rawpath, imgsavepath):
    imgs = os.listdir(imgpath)
    raw = os.listdir(rawpath)
    imgs.sort()
    raw.sort()

    # 将图片的开始和结尾放入img文件夹中
    for i in range(0, len(imgs), 2):
        begin = imgs[i].split('.')[0]
        end = imgs[i + 1].split('.')[0]
        # rawname = raw[i // 2].split('.')[0]
        for raw in range(int(begin), int(end)+1):
            if os.path.exists(rawpath + '%06d' % raw + '.jpg'):
                os.system('cp ' + rawpath + '%06d' % raw + '.jpg' + ' ' + imgsavepath)


mergeimg(imgpath, rawpath, imgsavepath)