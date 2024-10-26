import json

json_string =  '{"name" : "GeeksforGeeks", "Topic" : "Json to String", "Method": 1}'

data = json.loads(json_string)
print(data)
print("type of data is: {}".format(type(data)))

jsonfilepath = "C:/Users/GAKASH/Downloads/example_1.json"
file = open(jsonfilepath,"r")

data1 = json.load(file)
print("type of data is: {}".format(type(data1)))
print(data1)

file2 = open("newjson.json","w")
data = json.dump(data1,file2)

data2 = json.dumps(data)
print(type(data2))

# Multiple files handling

import os
path = "C:/Users/GAKASH/Downloads/data/datasource (1)/"
paths = os.walk(path)

for path,dir,file in paths:
    for f in file:
        path1 = os.path.join(path,f)

        print(path1)
        print(f)


# Multiple csv handling

from typing import final
import pandas as pd

try:
    df = pd.read_table("C:/Users/GAKASH/Desktop/u.user.txt",delimiter="|")
except Exception as e:
    print("error is {}".format(e))


import glob
import os

try:
    # files = glob.glob("C:/Users/GAKASH/Downloads/data/datasource (1)/New folder/*")
    files = os.walk("C:/Users/GAKASH/Downloads/data/datasource (1)/New folder/")
    for path,dir,file in files:
        for file in file:
            print(os.path.join(path,file))
            with open(os.path.join(path,file),"r") as f:
                data = f.read()
                with open("newoscsv.csv","a") as x:
                    data = x.write(data)

    
    with open("newoscsv.csv","r") as m:
        data = m.read()
        print(data)

except Exception as e:
    print(e)

cwd = os.getcwd() 
print(cwd)

os.chdir("C:/Users/GAKASH/Downloads/data/datasource (1)")
cwd = os.getcwd() 
print(cwd)


