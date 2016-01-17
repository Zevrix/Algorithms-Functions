L1 = [1]
from time import time
stime = time()
rows = int(input('How many rows? ', ))
mod = int(input('Mod what? ',))
print()

x = 1

h = 0
t = 0

count = 0


while x != rows+1:
    L2 = []
    if h == 1:
        print(x,L1)
    if t == 1:
        with open("Pascal.txt", "a") as text_file:
            print(x,L1,file = text_file)
    count = count + L1.count(0)
    for i in range(len(L1)-1):
        L2.append((L1[i]+L1[i+1])%mod)
    L2.append(1)
    L2.insert(0,1)
    L1 = L2
    x = x + 1

print()
print((rows*(rows+1))/2-count)
print()
print(time()-stime)
input()

#from row 1 to the row before the first 7**n triangle of 0s there are 28**n numbers not divisible by 7
