even = set(range(0, 40, 2))
print(sorted(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

print("=" * 100)

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

print("=" * 100)
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))
