import os

jsonpngpath = '/home/archer/Desktop/chapter4/frames/hy6/label_json/'
labelpath = '/home/archer/Desktop/chapter4/frames/hy6/label/'
jsons = os.listdir(jsonpngpath)
# labels = os.listdir(labelpath)
jsons.sort()
# labels.sort()

for i in jsons:
    if i.endswith('_json'):
        n = i.split('_')[0]
        os.system('cp ' + jsonpngpath + i + '/label.png' + ' ' + labelpath + n + '.png')
