# n+mlogp
import sys
input = sys.stdin.readline
def power(a,b):
    if b==0:
        return 1
    if b%2==0: 
        return (power(a,b//2)**2)%p
    else:
        return ((power(a,b//2)**2)*a)%p

p = 1000000007
fact = [1 for _ in range(4000001)]
for i in range(1,4000001):
    fact[i] = (fact[i-1]*i)%p

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = fact[n]%p
    b = (fact[k]*fact[n-k])%p
    print((a%p) * (power(b,p-2)%p) %p)