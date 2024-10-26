
data= {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
data2 = {

  "calories": [420, 380, 390],
  "duration": [50, 40, 45]

}

import json

file = open("new_json.json","w")

data1 = json.dump(data,file)

import os
print(os.listdir)
print(os.getcwd())
print(os.listdir())
os.rename("ShellCommands.py","Shell.py")
os.remove("dummy.py")
os.rmdir("newdir")
os.environ.get("path")

print(os.name)
print(os.environ)
print(os.getlogin())
os.mkdir("akash")

