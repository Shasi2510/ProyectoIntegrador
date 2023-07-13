import os
import readchar

key=n
n=os.system
b=1
for b in range (0,51):
    if key == readkey(n):
        os.system('cls' if os.name=='nt' else 'clear')
    print(b)
    