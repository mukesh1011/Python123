import os


listing = os.walk('.')
#print(sorted(listing))

for root, direcotories, files in listing:
    print(root)
    for d in direcotories:
        print(d)
    for file in files:
        print(file)