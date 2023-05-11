import cv2
print(cv2.__version__)
import matplotlib.pyplot as plt
# Read image
img = cv2.imread("./Lepton_1_Moment010.jpg")
if img is None:
    print('Image load failed')
    sys.exit()
sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
path = "ESPCN_x4.pb"
 
sr.readModel(path)
 
sr.setModel("espcn",4)
 
result = sr.upsample(img)
 
# Resized image
resized = cv2.resize(img,dsize=None,fx=3,fy=3)
 
plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
# Original image
plt.imshow(img[:,:,::-1])
plt.subplot(1,3,2)
# SR upscaled
plt.imshow(result[:,:,::-1])
plt.subplot(1,3,3)
# OpenCV upscaled
plt.imshow(resized[:,:,::-1])
plt.show()