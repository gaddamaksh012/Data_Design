

names = "prakash"
class akash:
    age = 25 # class variable
    def __init__(self,name,num):
        self.name  = name # instase variable
        self.num = num
   
    def result(self):
        print("name is {} and age is {}".format(self.name,akash.age))
        

    @staticmethod
    def static():
        stat_var = "100000"
        print("this is from static variable age is {} and {}".format(akash.age,stat_var))

    @classmethod
    def sky(cls):
        print("this is from class method name is {} {}".format(akash.age,names))

obj = akash("akash",100)
obj.result()
akash.static()
obj.sky()


# class A:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def A1(self):
#         print("this is from A class") 

# class B(A):
#     def B1(self,name,age):
#         print("this is from B1 class name is {} age is {}".format(self.name,self.age))
#         self.A1

# obj = B()
# obj.B1()
# obj.A1()

