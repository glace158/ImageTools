import os
import cv2
import random
import shutil

imageList = []
lineList = []
with open('E:/DataSet/FLIR_ADAS_v2/images_thermal_train/coco.json', 'r') as f:
    lines = ""
    print("Reading...")
    
    for line in f:
        lines += line
        
    print("Read End")
    lineList = lines.split('''},
    {''')
    imageList = [ i for i in lineList if ("video_id" in i)]
    print(imageList[0])
    lineList = [ i for i in lineList if i not in imageList]
    lineList = [ i for i in lineList if ('"category_id": 1,' in i)]
    print(lineList[0])
    
file_path = 'E:/DataSet/FLIR_ADAS_v2/images_thermal_train/data/'
move_path = './move4/'
print("Start")
file_list = os.listdir(file_path)
print(file_list)
file_len = len(file_list)
print("Start!!")
random_list = random.sample(file_list, 2000)

for i in range(len(random_list)):
    while True:
        is_in = False
        for image in imageList:
           
            if random_list[i] in image:
                imagelines = image.split(',')
                Id = [j.split()[1] for j in imagelines if ('"id":'in j)]
                print("\r"+ str(i) + ": " + str(Id), end='')     
                        
                for line in lineList:
                    if (('"image_id": ' + str(Id[0])) in line):
                        is_in = True
                        print("is_in")
                        break
                    else:
                        random_list[i] = random.sample(file_list, 1)[0]
            
            if is_in:
                break
    
        if is_in:
            break
            
random_list = list(set(random_list))

print(random_list)
count = 0
for file in random_list:
    
    shutil.move(file_path + file, move_path)
    
    if os.path.exists(move_path + file):
        count += 1
        print("\r"+ str(round(  count/len(random_list) * 100)) + "% " + str(count) + "/" + str(len(random_list)) + ": " + file + "Move!",end="")
        
        