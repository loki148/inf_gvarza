import matplotlib.pyplot as plt
import numpy as np
import os
from random import choice
os.chdir('c:/Users/admin/Desktop')

a = open('cisla.txt')
nums = [int(i) for i in a.read().split()]
x = 0.5 + np.arange(15)

colors = ['blue','red','magenta', 'green', 'black', 'yellow','blue','red','magenta', 'green', 'black', 'yellow','blue','red','magenta', 'green', 'white', 'yellow', ]
fig, ax = plt.subplots()
ax.bar(x, nums, width=1, edgecolor="white", linewidth=0.7, color= colors)
ax.set(xlim=(0, 15), xticks=np.arange(1, 15),
       ylim=(0, max(nums)), yticks=np.arange(1, max(nums)))

plt.show()
