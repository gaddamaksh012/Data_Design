# Ristriction the method
class car:
    # def __init__(self):
    #     self.__softwareinstallation()
    def driving(self):
        print("ths is from driving")
    def __softwareinstallation(self):
        print("this is from software")

obj = car()
obj.driving()


# ristricting the variables


class akash:
    __name = "akash"
    x = "abc"
    def __init__(self):
        __name = "pppp"
    def details(self):
        print("this is from details")
    def names(self,name):
        __name = name
        print(name)
obj1 = akash()
obj1.details()
obj1.names("Prakash")
print(obj1.x)
obj1.x = "xyz"
print(obj1.x)


