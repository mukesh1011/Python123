trees = ["Larch", "Larch"]
identified_trees = trees

trees.append("Horse Chestnut")
print(identified_trees)
print(trees)

flowers = [["rose", "red"],
           ["snapdragon", "white"],
           ["daisy", "white"],
           ["lily", "yellow"]
           ]

second_flowers = flowers

second_flowers[1] = ["lilac", 'purple']

second_flowers[1][1] = 'pink'
print(flowers)

even = range(0, 20, 2)

for number in even[::-1]:
    print(number, end=', ')