while True:
    try:
        a = int(input('zadaj cislo'))
        break
    except:
        print('musi byt cislo')

fib = [1,1]
for i in range(2,a):
    fib.append(sum(fib[(i-2):i]))

print(fib[-1])
