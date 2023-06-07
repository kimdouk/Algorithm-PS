def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
a,b = map(int,input().split())
lcm = (a//gcd(a,b))*b
print(gcd(a,b),lcm,sep='\n')