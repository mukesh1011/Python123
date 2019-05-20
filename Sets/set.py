farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 60)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

print("=" * 60)

even = set(range(0, 40, 2))

print(even)

square_tuple = (4, 6, 9, 16, 25)
square = set(square_tuple)
print(square)
