n = int(input())
data = [input() for _ in range(n)]
result = ''
for i in range(len(data[0])):
    tmp = set()
    for j in range(n):
        tmp.add(data[j][i])
    if len(tmp)==1:
        result+=data[j][i]
    else:result+='?'
print(result)