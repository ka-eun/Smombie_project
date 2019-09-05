import os
path = ""

for i, fname in enumerate(os.listdir(path)):
    fullpath = path+fname
    new_name = fname.replace(" (", "_")
    new_name = new_name.replace(")", "")
    newpath = path+new_name
    os.rename(fullpath, newpath)
