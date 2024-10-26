import os
import sys
print(os.getcwd())
os.mkdir("d:\\newdir")  
print(os.name)   
os.chdir("d:\\")  
os.rmdir("d:\\newdir")  
os.chdir("..")  
os.rmdir("newdir")  

import sys    
    
path1 = os.access("Python.txt", os.F_OK)     
print("Exist path:", path1)


files = os.walk("C:/Users/GAKASH/Desktop/vscode/PythonPractise/")
for path,dir,file in files:
    for file in file:
        print(os.path.join(path,file))   
        print(file)   

os.mkdir("C:\MyPythonProject")
os.chdir("C:\MyPythonProject") # changing current workign directory
os.rmdir("C:\\MyPythonProject")

print(os.listdir("C:/Users/GAKASH/Desktop/vscode/PythonPractise/"))
python_files = []
for file in os.listdir("C:/Users/GAKASH/Desktop/vscode/PythonPractise/"):
    if file.endswith(".py"):
        python_files.append(file)
        os.system("python {}".format(file))
        break

print (python_files)


x = 0
assert x > 0, 'Only positive numbers are allowed'
print('x is a positive number.')

import sys
print(sys.path)

import subprocess
file = "Oops.py"
data = subprocess.check_output(file, shell=True)

data = data.decode("UTF-8")

print(data)



