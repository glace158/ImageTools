import os
import cv2
import random
import shutil

file_path = 'C:/Users/11/Downloads/thermal_3.v10i.yolov5pytorch/train/images/'
move_path = './move3/'
print("Start")
file_list = os.listdir(file_path)
print(file_list)
file_len = len(file_list)
print("Start!!")
random_list = random.sample(file_list, 70)
print(random_list)
count = 0
for file in random_list:
    shutil.move(file_path + file, move_path)
    
    if os.path.exists(move_path + file):
        count += 1
        print("\r"+ str(round(  count/len(random_list) * 100)) + "% " + str(count) + "/" + str(len(random_list)) + ": " + file + "Move!",end="")