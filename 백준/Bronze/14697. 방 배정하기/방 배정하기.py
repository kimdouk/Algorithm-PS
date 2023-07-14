from math import ceil
import sys
a,b,c,n = map(int,input().split())
for i in range(ceil(n/a)+1):
    for j in range(ceil(n/b)+1):
        for k in range(ceil(n/c)+1):
            if i*a + j*b + k*c == n:
                print(1)
                sys.exit()
print(0)