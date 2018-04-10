import random
a = 10000
m = []
for i in range(0,a):
    n = random.randrange(1,7)
    m.append(n)
print(m)
k = sum(m)
print(k/a)
