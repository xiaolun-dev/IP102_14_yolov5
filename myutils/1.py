import codecs
import os
import shutil
# Path1 = '/root/autodl-tmp/Yolov5_IP102/images/'
# Path2 = '/root/autodl-tmp/Yolov5_IP102/labels/'
rootPath1 = '/root/autodl-tmp/Yolov5_IP102/train/images/'
rootPath2 = '/root/autodl-tmp/Yolov5_IP102/train/labels/'
# List1 = os.listdir(Path1)
# List2 = os.listdir(Path2)
imageNamesList = os.listdir(rootPath1)
labelNamesList = os.listdir(rootPath2)
# print(len(List1))
# print(len(List2))
print(len(imageNamesList))
print(len(labelNamesList))
# for i in range(len(imageNamesList)):
#     # print(i)
#     # labels = i[:-4]+'.txt'
#     shutil.move(rootPath1+imageNamesList[i],Path1+imageNamesList[i])
#     shutil.move(rootPath2+labelNamesList[i],Path2+labelNamesList[i])