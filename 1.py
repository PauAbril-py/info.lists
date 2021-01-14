import random

l = ['Xavier','Jordi','Ángel','Tomas','Lluís','Remei','Jordi']

l.append('Josep')

l.pop(0)
l.pop(1)

l.insert(l.index('Tomas'), 'TomAs')
l.remove('Tomas')
print(l)

print(l.count('Jordi'))

l.sort()

for i in range(l.count('Jordi')):
	l.remove('Jordi')

x = []
while len(x) != len(l):
	y = random.choice(l)
	if y not in x:
		print(y)
		x.append(y)


print(l)