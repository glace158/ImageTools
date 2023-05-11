import os
import time
import cv2
start = time.time()

file_path = './move4/'
file_list = os.listdir(file_path)
print(file_list)
file_len = len(file_list)
count = 0
for file in file_list:
    try:
        img=cv2.imread(file_path + file)
        result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(file_path + file , result)
        count += 1
        
        print("\r" + str(round(count / file_len * 100, 2)) + "% " + str(count) + "/" + str(file_len) + ": " + file + "Resolution Complete!", end="")
        
    except:
        print(file + "Resolution Failed")
    
end = time.time()
print(f"{end - start:.5f} sec")
