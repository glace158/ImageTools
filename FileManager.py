import os
import os.path, time
path = 'C:/Users/11/Desktop/LeptonCapture/'

path2 = 'C:/Users/11/Desktop/LeptonCapture2/'
file_list = os.listdir(path)
file_list2 = os.listdir(path2)

file_set = set(file_list) - set(file_list2)
print(file_set)

file_set = set(file_list2) - set(file_list)
print(file_set)

file_set = set(file_list2) & set(file_list)

created_dict = {}
modified_dict = {}

for file in file_set:
    modified_dict[file] = time.ctime(os.path.getmtime(path+file))
    created_dict[file] = time.ctime(os.path.getctime(path+file))

change_file_list =[]
for file in file_set:
    is_modified = False
    is_modified = not( modified_dict[file] == time.ctime(os.path.getmtime(path2+file)))
    
    if is_modified:
        change_file_list.append(file)
        
print(change_file_list)