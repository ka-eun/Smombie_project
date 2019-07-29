import os



path = "E:\\real-darkflow-master\\new_model_data\\smombie\\"
# new_path = "E:\\real-darkflow-master\\new_model_data\\new_smombie\\"


n=0
for filename in os.listdir(path):
    os.rename(path + filename, path + filename[:-4] + ".png")
    #os.rename(path+filename, path+filename+".png")
    n+=1
