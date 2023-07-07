h,m,s = map(int,input().split())
sec = int(input())
s += (sec%60)
m += s//60
m += sec//60
s %=60

h+= (m//60)
m %=60

h%=24
print(h,m,s)