import os

path = 'C:/Users/11/Downloads/thermal_3.v10i.yolov5pytorch/train/labels/'

#path = 'C:/Users/11/Downloads./PersonDection.v2i.yolov5pytorch/train/test/'

#path = 'C:/Users/11/Videos/LeptonCaptures/UNKNOWN/'

file_list = os.listdir(path)
#print(file_list)

for i in file_list:
    f = open(path + i)
    inp = f.read()
    
    if inp != '':
        classNumList = inp.split('\n')
        lines = []
        for j in classNumList:
            lines.append("person" + j[1:])
        
        with open(path+i, 'w') as f:
            for line in lines:
                f.write(line+"\n")
            
print("Done")
#file_list_py = [file for file in file_list] 

#print(type(file_list_py[0]))

