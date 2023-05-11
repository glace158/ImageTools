import os

num = 2534
path = 'C:/Users/11/Downloads./PersonDection.v4i.yolov5pytorch/train/labels/'
#path = 'C:/Users/11/Downloads./PersonDection.v4i.yolov5pytorch/train/test/'

#path = 'C:/Users/11/Videos/LeptonCaptures/UNKNOWN/'

file_list = os.listdir(path)
#print(file_list)

for i in file_list:
    f = open(path + i)
    #print("-----------------------------------------------------------------")
    inp = f.read()
    
    if inp != '':
        classNumList = inp.split('\n')
        
        for j in classNumList:
            if j[0] != '1':
                print("something worng", i)

print("Done")
#file_list_py = [file for file in file_list] 

#print(type(file_list_py[0]))
