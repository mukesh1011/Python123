menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "spam", "sausage", "bacon"])
menu.append(["spam", "bacon", "sausage", "bacon"])
menu.append(["span", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#print(menu)

for meal in menu:
    if not "spam" in meal:
        for i in meal:
            print(i)