fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour,  green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprout": "mm, lovely",
       "spinach": "can't I have some more fruit, please"}

print(veg)

veg.update(fruit)
print(veg)

print("-" * 40)

nice_nasty = fruit.copy()
nice_nasty.update(veg)
print(nice_nasty)

print(fruit)
print(veg)

