# def func(*var):
#    for i in var:
#        print(i)
#
# func(20,2)
#
# lst = ["a","b"]
# lst1 = [12,2,3]
# lst2 = [4,5,6]
# for i in enumerate(lst,start=1):
#     print(i)
#
# for (x,y) in zip(lst1,lst2):
#     print(x+y)
#
# def check_distinct(l1):
#     if len(l1) == len(set(l1)):
#         return True
#     else:
#         return False
#
# print(check_distinct([1,2,3,4,7]))
#
# list1 = ['s', 'r', 'a', 's']
# list2 = ['a', 'a', 'n', 'h']
# x = ["".join([i, j]) for i, j in zip(list1, list2)]
# print(x)


class A(object):
    def __init__(self, a):
        self.num = a

    def mul_two(self):
        self.num *= 2

class B(A):
    def __init__(self, a):
        A.__init__(self, a)

    def mul_three(self):
        self.num *= 3


obj = B(4)
print(obj.num)

obj.mul_two()
print(obj.num)

obj.mul_three()
print(obj.num)


