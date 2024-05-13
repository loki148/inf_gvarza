from random import randint

a = []
for _ in range(30):
    a.append(randint(0,10000))


par = 0
sedem = 0
for i in a:
    if i % 2 == 0:
        par +=1
    if i % 7 == 0:
        sedem +=1

print('parne:', par)
print('parne:', 30-par)
print('delitelne siedmimi:', sedem)

