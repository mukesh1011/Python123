name = input("Print your name: ")
age = int(input("Print your age: "))

if 18 > age > 31:
    print("Welcome to the holiday, {0}".format(name))
else:
    print("Sorry {}, you are not allowed to holiday".format(name))