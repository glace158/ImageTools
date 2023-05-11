import os
import time
import cv2
start = time.time()

file_path = 'C:/Users/11/Videos/LeptonCaptures/DATA/'
file_list = os.listdir(file_path)
file_list = [ file for file in file_list if ".jpg" in file]
print(file_list)
file_len = len(file_list)
count = 0
#file_list.reverse()
for file in file_list:
    try:
        img=cv2.imread(file_path + file)
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        model_list = ["EDSR", "FSRCNN", "ESPCN", "LapSRN"]
        model_name = model_list[2]
        size = 4
        path = model_name + "_x" + str(size) + ".pb"
        sr.readModel(path)
        sr.setModel(model_name.lower(), size)
        result = sr.upsample(img) # upscale the input image
        
        
        #result = sr.upsample(result) # upscale the input image
        
        cv2.imwrite(file_path + "Result/" + file , result)
        count += 1
        #print(file + "Resolution Complete!", end="")
        print("\r" + str(round(count / file_len * 100, 2)) + "% " + str(count) + "/" + str(file_len) + ": " + file + "Resolution Complete!", end="")
        
        
    except:
        print(file + "Resolution Failed")
    
end = time.time()
print(f"{end - start:.5f} sec")