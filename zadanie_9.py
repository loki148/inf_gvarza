from random import randint

hody = []
for _ in range(3):
    hody.append(randint(1,6))



if hody.count(hody[1]) == 3:
    print('vyhra')
elif hody.count(hody[1]) == 2 or hody.count(hody[2]) == 2:
    print('skoro')
else:
    print('whomp whomp')