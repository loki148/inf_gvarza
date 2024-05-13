a = int(input())

delitele = []
for i in range(1,a):
    if a % i ==0:
        delitele.append(i)

if sum(delitele)==a:
    print('dokonalé číslo')

