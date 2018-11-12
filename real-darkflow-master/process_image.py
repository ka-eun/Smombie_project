import os



path = "D:\\darkflow-master\darkflow-master\\new_model_data\\smombie\\"
new_path = "D:\\darkflow-master\\darkflow-master\\new_images\\"


n=0
for filename in os.listdir(path):
    os.rename(path+filename, new_path+str(n)+".png")
    n+=1