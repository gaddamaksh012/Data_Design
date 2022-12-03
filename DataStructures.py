# List operations

list1 = [1,2,3,4]
list1.append(4)
list1[0] = 5
list1.pop()
list1.insert(3,3)
list1.sort()
# print(list1)

# Sets operation

set1 = {1,3,6,7,5,2,9,9,3}
set2 = {200,300,10,40,0,500}

set1.add(100)

set2.remove(3000)
set2.discard(3000)
print(set1)
for x in set1:
    print(x)
set3 = set1.union(set2)
print(set3)
set1.update(set2)

# Distionary Operations

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["brand"]
thisdict["brand2"] = "suziki"

thisdict.get("brand2")

thisdict.update({"brand2":"Balino"})


thisdict.pop("brand2")

for x in thisdict:
    print(thisdict[x])
print(thisdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])

for i in myfamily:
    for k in myfamily[i]:
        print(myfamily[i][k])


d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}

for k,v in d2.items():
    d1[k]=v

print(d1)

from collections import ChainMap
d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D2":"Hello"}
map=ChainMap(d2,d1)
print(map)

dict1 = { key:value for i in (d1,d2) for key,value in i.items() }

dct2 = {**d1,**d2}
print(dct2)
print(dict1)
        