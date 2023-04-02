import random

n = 7
tt = []
for i in range(n):
    tt[i] = int(random(1,5))
print (tt)

for i in range(n):
    if tt[i] == 5: 
        tt[i] == 1
    elif tt[i] == 4: 
        tt[i] == 2
print (tt)
