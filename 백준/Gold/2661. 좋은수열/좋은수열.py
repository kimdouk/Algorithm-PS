import sys
n = int(input())
result = []
def isgood(arr):
    for i in range(1,len(arr)//2+1):
        if arr[-i:]==arr[-i*2:-i]:return False
    return True
            
def dfs():
    global result
    if len(result)==n:
        print(''.join(map(str,result)))
        sys.exit()
    for i in range(1,4):
        result.append(i)
        if isgood(result):
            dfs()
            result.pop()
        else:
            result.pop()
dfs()