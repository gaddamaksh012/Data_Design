def lowercase(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower
        return string_lowercase
    return wrapper()

def splitting(function):
    def wrapper2():
        func = function()
        split = func.split()
        return split
    return wrapper2()
@splitting
@lowercase
def result():
    return "Hello World"
print(result)

