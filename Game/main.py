# import player
from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

tim = Player("Tim")
# print(tim.name)
# print(tim.lives)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim._lives = 9
# print(tim)
#
# tim.level = 2
# print(tim)
#
# tim.level += 5
# print(tim)
#
# tim.level = 3
# print(tim)
#
# tim.score = 500
# print(tim)

# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print(brother)
#
# brother.take_damage(13)
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp1 = Vampyre("vamp1")
# print(vamp1)
#
# vamp1.take_damage(5)
# print(vamp1)
#
# vamp1.take_damage(8)
# print(vamp1)
#
# print("=" * 100)
#
# another_troll.take_damage(30)
# print(another_troll)
#
# while vamp1._alive:
#     vamp1.take_damage(1)

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)



