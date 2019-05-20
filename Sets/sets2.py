even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuple = (4, 6, 9, 16, 25)
square = set(square_tuple)
print(square)
print(len(square))

print(even.union(square))
print(len(even.union(square)))

print("=" * 100)

print(even.intersection(square))
print(even & square)

print(square.intersection(even))
print(square & even)