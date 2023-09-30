es,ss,ms = map(int,input().split())
e,s,m = 1,1,1
for i in range(1,15*28*19+1):
    if es==e and s==ss and m==ms:
        print(i)
        break
    e+=1; s+=1; m+=1;
    if e>15:e%=15
    if s>28:s%=28
    if m>19:m%=19