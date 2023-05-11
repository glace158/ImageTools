import os

num = 0
#path = 'C:/Users/11/Videos/LeptonCaptures/DATA/'
#path = 'C:/Users/11/Downloads/PersonDection.v8i.yolov5pytorch/valid/images/Result/'
path = 'C:/Users/11/Downloads./PersonDection.v9i.yolov5pytorch/test/labels/'

file_list = os.listdir(path)
file_list_py = [file for file in file_list] 

print(type(file_list_py[0]))

for name in file_list_py:
    src = os.path.join(path, name)
    namelist = name.split('.')
    dst = namelist[0]+".rf."+ str(num) +".txt"
    dst = os.path.join(path, dst)
    os.rename(src, dst)
    num+=1