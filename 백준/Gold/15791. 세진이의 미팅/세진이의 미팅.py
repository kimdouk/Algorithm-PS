def power(a,b):
    if b==0:
        return 1
    if b%2:
        return ((power(a,b//2)**2)*a)%p
    else:
        return (power(a,b//2)**2)%p

p = 1000000007
fact = [1 for _ in range(1000001)]
for i in range(1,1000001):
    fact[i] = (fact[i-1] *i)%p
n,m = map(int,input().split())
a = fact[n]
b = (fact[n-m]*fact[m])%p
print(((a%p)*(power(b,p-2)%p))%p)