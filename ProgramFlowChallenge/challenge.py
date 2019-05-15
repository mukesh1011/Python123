ipaddress = input("Enter IP Address: ")

if ipaddress != '':
    if ipaddress[0] == '.':
        seg = 0
    else:
        seg = 1

    for i in range(0, len(ipaddress)):
        if ipaddress[i] in '.':
            seg += 1
            continue

    if ipaddress[len(ipaddress)-1] == '.':
        seg -=1

else:
    seg = 0
print("Number of segment is {}".format(seg))
