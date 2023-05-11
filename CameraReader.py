import os
import re
import numpy as np
import cv2
import atexit
    
file_path = os.getcwd()
print(file_path)
file_list = os.listdir(file_path)
print(file_list)
last_file_num = 0

for file in file_list:
    result = re.search("Lepton_([0-9]+).mp4", file)
    if result:
        file_num = result.group(1)
        last_file_num = int(file_num) if last_file_num < int(file_num) else last_file_num

print(last_file_num)
sr = cv2.dnn_superres.DnnSuperResImpl_create()
path = "ESPCN_x4.pb"
sr.readModel(path)
sr.setModel("espcn", 4) # set the model by passing the value and the upsampling ratio


try:
    print("Camera Running..")
    cap = cv2.VideoCapture(0)

    fps = 20.0
    width = int(cap.get(3)) * 4
    height =int(cap.get(4)) * 4
    print(width, height )
    fcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('Lepton_' + str(last_file_num + 1) + '.mp4', fcc, fps, (width, height))
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Video Error")
            break
        
        
        frame = sr.upsample(frame)
        #frame = cv2.resize(frame, (width,height))
        cv2.imshow('video', frame)
        out.write(frame)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print("Camera End")
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
except:
    print("Camera Fail..")
    


    

