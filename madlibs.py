# String concatnation 
# name  = input("enter ypu name: ")
# print("my name is "+name)
# print("my name is {}".format(name))
# print(f"my name is {name}")

# name  = input("enter ypu name: ")
# village = input("Enter your village: ")
# intrest = input("Enter your intrest: ")

# madlib = f" my name is {name} and I am from {village} and I am very,uch intrested in {intrest}"

# print(madlib)


import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x} : "))
        if guess > random_number:
            print(f"sorry its too high {guess}")
        elif guess < random_number:
            print(f"sorry its too low {guess}")

    print(f"your guess is correct {random_number}")

guess(10)


# def usernum(y):
#     user_num = random.randint(1,y)
    