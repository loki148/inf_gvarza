from random import choice

big = list('abcdefghijklmnoprstquvwxyz'.upper())
small = list('abcdefghijklmnoprstquvwxyz')
nums = list('1234567890')

print(''.join([choice(small),choice(small),choice(nums),choice(nums),choice(big),choice(big)]))