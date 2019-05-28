import shelve

with shelve.open("ShelfTest") as fruit:
    fruit['orange'] = "s sweet, orangem citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus"
    fruit['grape'] = "a small , sweer fruit growing in bunches"
    fruit['lime'] = "a sour green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)