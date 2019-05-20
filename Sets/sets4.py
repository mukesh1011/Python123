even = set(range(0, 40, 2))
print(even)

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(squares)

squares.discard(4)
squares.discard(16)
squares.discard(8)
print(squares)
squares.remove(8)