import math
m,n = map(int,input().split())
isPrime = [True] * (n+1)
isPrime[1] = False
for i in range(2,int(math.sqrt(n)+1)):
    if isPrime[i]:
        j = 2
        while j*i<=n:
            isPrime[i*j] = False
            j+=1
result = [i for i in range(m,n+1) if isPrime[i]]
print(*result,sep='\n')