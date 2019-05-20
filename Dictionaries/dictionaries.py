fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour,  green citrus fruit"}

print(fruit)
print(fruit["orange"])
print(fruit["lime"])

fruit["pear"] = "an odd shaped apple"
print(fruit)

fruit["lime"] = "great with tequila"
print(fruit)

del fruit["lemon"]
print(fruit)
# fruit.clear()
# print(fruit)

#print(fruit["tomato"])

# while True:
#     dict_key = input("Enter a fruit: ")
#     if dict_key == "quit":
#         break
#     desciption = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(desciption)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("We don't have a " + dict_key)

for snack in fruit:
    print(fruit[snack])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

for val in fruit.values():
    print(val)

print("-" * 40)
for key in fruit:
    print(fruit[key])

