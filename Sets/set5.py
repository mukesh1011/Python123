even = set(range(0, 40, 2))
print(even)

square_tuple = (4, 6, 16)
squares = set(square_tuple)
print(squares)

if squares.issubset(even):
    print("Squares is a subset of even")
if even.issuperset(squares):
    print("Even is a subset of square")