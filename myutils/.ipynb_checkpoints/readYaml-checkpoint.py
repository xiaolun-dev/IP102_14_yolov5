import yaml
import os
Path = '/root/autodl-tmp/Yolov5_IP102'
strList = []
def read_yaml():
    with open(Path+"/data.yaml", encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        print(data['names'])
#         strList = data['names'][:14]
        print(strList)
#     for i in strList:
#         print(i)
#         path = Path+'/'+i
#         imagesDir = Path+'/'+i+'/images'
#         labelsDir = Path+'/'+i+'/labels'
#         folder = os.path.exists(path)
#         if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
#             os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
#             os.makedirs(imagesDir) 
#             os.makedirs(labelsDir)  
#             print ("---  new folder...  ---")
#             print ("---  OK  ---")
#         else:
#             print ("---  There is this folder!  ---")    
    
read_yaml()