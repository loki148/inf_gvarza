a = int(input())
def pent(num):
    digits = []
    while num:
        digits.append(int(num % 5))
        num //= 5
    return '0p'+''.join([str(i) for i in digits[::-1]])

print(bin(a),pent(a),oct(a))