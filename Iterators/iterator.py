# string = "1234567890"
#
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

my_iterator = iter(numbers)

for i in range(len(numbers)):
    next_item = next(my_iterator)
    print(next_item)

