n = int(input())
m = int(input())
ioi = input()
p = ('IO'*n) + 'I'
result = 0
for i in range(len(ioi)-(2*n)):
    if p == ioi[i:i+(2*n+1)]:
        result +=1
print(result)