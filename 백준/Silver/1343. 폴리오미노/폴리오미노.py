data = list(input().split('.'))
flag = 0
result = ''
for i in data:
    if len(i)%2!=0:
        flag = 1
        break
    a,b = len(i)//4, len(i)%4
    result+= a*'AAAA'+b*'B'
    result+='.'
print(-1 if flag else result[:-1])