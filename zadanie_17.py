rodnec = list(input())

if int(rodnec[2]) > 1:
    female = True
    print('pohlavie: zena')
    rodnec[2]= str(int(rodnec[2]) -50)
else:
    print('pohlavie: muz')
rodnec ="".join(rodnec)
print(f"{rodnec[4:6]}.{rodnec[2:4]}.19{rodnec[0:2]}")


