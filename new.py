with open("problem.txt","r") as f:
    data = f.read().splitlines()
    # print(data)
    new_lst = []
    c = 0
    for i in data:
        if ":" in data[c]:
            elements = data[c].split(":")
            tuple1 = tuple(elements)
            new_lst.append(tuple1)
        c = c+1

print(new_lst)
Dict1 = dict((sublist[0], sublist[1:]) for sublist in new_lst)
print(Dict1)

dict1 = dict(new_lst)
print(dict1)
# print(dict1.get("machiene "))

str1 = ["akasj","prkash"]
for i in str1:
    i = "{}/".format(i)
    print(i)
