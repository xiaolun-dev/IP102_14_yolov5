import codecs
import os
import shutil
DirList = ['rice_leaf_roller', 'rice_leaf_caterpillar', 'paddy_stem_maggot', 'asiatic_rice_borer', 'yellow_rice_borer', 'rice_gall_midge', 'rice_stemfly', 'brown_plant_hopper', 'white_backed_plant_hopper', 'small_brown_plant_hopper', 'rice_water_weevil', 'rice_leafhopper', 'grain_spreader_thrips', 'rice_shell_pest']
# TxtTrainPath = '/root/autodl-tmp/Yolov5_IP102/train/images'
# TxtTestPath = '/root/autodl-tmp/Yolov5_IP102/test/labels'
rootPath1 = '/root/autodl-tmp/Yolov5_IP102/images'
rootPath2 = '/root/autodl-tmp/Yolov5_IP102/labels'
rootPath3 = '/root/autodl-tmp/Yolov5_IP102/test/images'
rootPath4 = '/root/autodl-tmp/Yolov5_IP102/test/labels'
rootPath5 = '/root/autodl-tmp/Yolov5_IP102/val/images'
rootPath6 = '/root/autodl-tmp/Yolov5_IP102/val/labels'
list1 = os.listdir(rootPath1)
list2 = os.listdir(rootPath2)
list3 = os.listdir(rootPath3)
list4 = os.listdir(rootPath4)
list5 = os.listdir(rootPath5)
list6 = os.listdir(rootPath6)
print(len(list1))
print(len(list2))
print(len(list3))
print(len(list4))
print(len(list5))
print(len(list6))
# labelNamesList = os.listdir(TxtTestPath)
# print(len(labelNamesList))
# labelNamesList2 = os.listdir(TxtTestPath)
# print(len(labelNamesList2))
# labelNamesList = labelNamesList1 + labelNamesList2
# print(len(labelNamesList))
# print(int(labelNamesList[2][2:5]))
# print(DirList[0])
# list = []
# num = 0
# for filename in DirList:
#     for i in os.listdir(rootPath+filename+'/labels'):
#         (name,extension) = os.path.splitext(i)
#         name = name +'.jpg'
#         shutil.copy(rootPath+filename+'/images/'+name,rootPath+'images/'+name)
#         shutil.copy(rootPath+filename+'/labels/'+i,rootPath+'labels/'+i)
# f = codecs.open('data.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
# line = f.readline()   # 以行的形式进行读取文件
# list1 = []
# while line:
#     a = line.split()
#     b = a[2:3]   # 这是选取需要读取的位数
#     list1.append(b)  # 将其添加在列表之中
#     line = f.readline()
# f.close()

# for i in list1:
#     print(i)