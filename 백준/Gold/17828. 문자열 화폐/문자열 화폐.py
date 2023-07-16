from string  import ascii_uppercase
alpha = ascii_uppercase
n,x = map(int,input().split())
result = ''
if n*26<x or n>x:
    print('!')
else:
    for i in range(n):
        if x-1>26*(n-i-1):
            print(alpha[x-(26*(n-i-1))-1],end='')
            x -= (x-(26*(n-i-1)))
        else:
            print(alpha[0],end='')
            x-=1