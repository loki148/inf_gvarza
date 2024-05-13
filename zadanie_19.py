import math
a,b,c = [int(num) for num in input().split()]

d = b**2 - 4*a*c

if d < 0:
    print('nemá riešenie')
elif d == 0:
    x = (-b+math.sqrt(d))/(2*a)
    print(f"koren je: {x}")
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(f"korene su: {x1}, {x2}")
    