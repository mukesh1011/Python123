age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age)) #replacement field

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7} ".format(31,"January","march", "may", "July", "August", "October", "December")) #replacement field

print("My age is %d years" % age) #string formatting
print("My age is %d %s, %d %s" %(age,"years", 6, "months")) #string formatting

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i **3)) #string formatting

print("Pi is approximately %12f" % (22/7)) #string formatting
print("Pi is approximately %12.50f" % (22/7)) #string formatting

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}" .format(i, i ** 2, i **3)) #replacement field

print("Pi is approximately  {0:12.50}" .format(22/7)) #replacement field