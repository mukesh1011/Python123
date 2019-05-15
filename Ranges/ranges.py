#print(range(100))

# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)
#
# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])

odd = range(0, 10000, 2)
print(odd)
print(odd[985])

sevens = range(7, 1000000, 7)
x = int(input("Enter number: "))

if x in sevens:
    print("{} is divisible by seven".format(x))

small_decimals = range(0, 10)
print(small_decimals)

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(6))