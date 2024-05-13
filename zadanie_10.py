import os
os.chdir('c:/Users/admin/Desktop')

a = open('text.txt', 'r')
con =a.read()
a.close()
print(len(con))
print(con.count('k'))

print(con)
con = con.replace('k', 'm')
print(con)

a = open('text.txt', 'w')
a.write(con)