import os
from readchar import readkey, key

b=1
for b in range (0,51):
    k = readkey()
    if k == key.N:
        os.system('cls' if os.name=='nt' else 'clear')
    print(b)
     