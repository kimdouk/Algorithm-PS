g,s = map(int,input().split())
W = input()
S = input()
wlist = [0 for _ in range(58)]
slist = [0 for _ in range(58)]
for char in W:
    wlist[ord(char)-65]+=1
length, start = 0,0
cnt = 0
for i in range(s):
    length+=1
    slist[ord(S[i])-65]+=1
    if length==g:
        if wlist == slist:
            cnt+=1
        slist[ord(S[start])-65]-=1
        length-=1
        start +=1
print(cnt)