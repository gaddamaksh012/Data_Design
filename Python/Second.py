import pandas as pd
df = pd.read_csv("C:/Users/GAKASH/Desktop/vscode/Target_file.csv")

print(df)
import os
path = "C:/Users/GAKASH/Downloads/data/datasource (1)/"
paths = os.walk(path)

for path,dir,file in paths:
    for f in file:
        path1 = os.path.join(path,f)

        print(path1)
        print(f)


import json
import requests
 
# Get dummy data using an API
res = requests.get("http://dummy.restapiexample.com/api/v1/employees")
 
# Convert data to dict
data = json.loads(res.text)
 
# Convert dict to string
data = json.dumps(data)
 
print(data)
print(type(data))

a =  {"name" : "GeeksforGeeks", "Topic" : "Json to String", "Method": 1}


for i in a.items():
    # print(i.get("Topic"))
    print(i.values())

    # for l in i:
    #     print(l)
 