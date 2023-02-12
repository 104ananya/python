def greet_user(name):  # parameter
    print(f"Hi {name}")
    print("Welcome")


print("Start")
greet_user("panda")  # positional argument
print("Finish")


# in case of keyword argument -- order doesn't matter while passing argument
# first positional then use keyword argument

def squ(num):
    print(num * num)


print(squ(5))

# try except block