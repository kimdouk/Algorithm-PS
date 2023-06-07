from math import ceil
a,b,v = map(int,input().split())
if a==v:print(1)
else:print(ceil((v-a)/(a-b))+1)