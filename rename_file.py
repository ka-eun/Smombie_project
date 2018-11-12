Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> path = "C:\\Users\\kauns\\Desktop\\Photos\\"
>>> for i, fname in enumerate(os.listdir(path)):
	fullpath = path+fname
	new_name = "00_"+str(i)+".jpg"
	print(fname, new_name)
	os.rename(path+fname, path+new_name)
 
 
