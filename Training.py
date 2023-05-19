colors = {'red'}
print(type(colors))
colors = {'red':'green'}
print(type(colors))
colors = ('red',)
print(type(colors))
print(colors)
colors = ['red',]
print(type(colors))
print(*colors)

from random import randint
x = randint(0, 100)
print(x)

for i in range(-5,0):
    print(i, end ="")
print()
    
    
