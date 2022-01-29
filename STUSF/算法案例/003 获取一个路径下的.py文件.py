from fileinput import filename
import os
url="./算法案例"
file_list=os.listdir(url)
for file_name in file_list:
    if(file_name.endswith(".py")):
        print(file_name)
