import os


path = '/home/archer/Desktop/chapter4/frames/hy2/label_json/'
json = os.listdir(path)
json.sort()
for i in json:
    os.system('labelme_json_to_dataset ' + path + i)
