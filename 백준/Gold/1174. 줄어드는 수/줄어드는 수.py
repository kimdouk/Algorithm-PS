temp_result = []
result = []
def dfs():
    if len(temp_result)>0:
        result.append(int(''.join(map(str,temp_result))))
        #return xxx
    for i in range(0,10):
        if len(temp_result)==0 or temp_result[-1]>i:
            temp_result.append(i)
            dfs()
            temp_result.pop()
dfs()
result.sort()
n = int(input())
if n>len(result):print(-1)
else:print(result[n-1])