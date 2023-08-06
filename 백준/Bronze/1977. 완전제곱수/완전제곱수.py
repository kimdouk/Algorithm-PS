a,b = int(input()), int(input())
result = []
for num in range(a,b+1):
    if int(num**(1/2)) - num**(1/2)==0:
        result.append(num)
if result:print(sum(result),sorted(result)[0],sep='\n')
else:print(-1)