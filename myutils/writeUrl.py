# -*- coding: utf-8 -*-
import os
#用getcwd()获取当前目录
# trainfiledir = "/root/autodl-tmp/Yolov5_IP102/train/images/"
# trainfiledir = "/root/autodl-tmp/Yolov5_IP102/test/images/"
trainfiledir = "/root/autodl-tmp/Yolov5_IP102/val/images/"
#获取目录列表
filenames=sorted(os.listdir(trainfiledir))
#以写的方式打开一个文本
f=open('/root/autodl-tmp/Yolov5_IP102/val_list.txt','w+')
#for循环
for filename in filenames:
    print(filename)
    filepath = trainfiledir+filename
    dir = filepath + '\n'
    # 把dir写到1.txt文本里面
    f.writelines(dir)
f.close()