__import__('sys').stdin.readline
n = int(input())
enter = [input() for _ in range(n)]
exit = [input() for _ in range(n)]
cnt = 0
for i in range(len(exit)):
    if exit[i]!= enter[i]:
        cnt+=1
        idx = enter.index(exit[i])
        enter = [enter[idx]]+enter[:idx]+enter[idx+1:]
print(cnt)