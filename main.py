import os
import shutil

from_dir = "C:/Users/stanz/Downloads"
to_dir = "C:/Users/stanz/OneDrive/Pictures"

list_of_files = os.listdir(from_dir)
for file in list_of_files :
    name,ext = os.path.splitext(file)
    if ext == "" :
        continue
    if ext in [".doc",".docx",".pdf"] :
        path1 = from_dir + "/" + file 
        path2 = to_dir + "/" + "doc_files"
        path3 = to_dir + "/" + "doc_files" + file
        if os.path.exists(path2) :
            print("Moving "+ file)
            shutil.move(path1,path2)
        else :
            os.makedirs(path2)
            print("Moving "+ file)
            shutil.move(path1,path2)
