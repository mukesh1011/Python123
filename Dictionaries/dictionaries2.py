fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour,  green citrus fruit"}

print(fruit)

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

print(fruit.items())
f_tuples = tuple(fruit.items())
print(f_tuples)

print("-" * 40)

for snack in f_tuples:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuples))