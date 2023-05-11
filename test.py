import os

num = 0
path = 'C:/Users/11/Videos/LeptonCaptures/DATA/'
#path = 'C:/Users/11/Videos/LeptonCaptures/TestSet/'
#path = 'C:/Users/11/Videos/LeptonCaptures/UNKNOWN/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.startswith('L')] 

for file in file_list:
    file_num = file.split('.')[0]
    file_num = file_num[:-1] if file_num[-1] == 'e' else file_num
    try:
        if int(file_num) > num:
            num = int(file_num) 
    except:
        pass
print(num)
print(type(file_list_py[0]))

for name in file_list_py:
    num += 1
    src = os.path.join(path, name)
    dst = str(num).zfill(4) + ".jpg"
    dst = os.path.join(path, dst)
    os.rename(src, dst)
    
