from collections import deque
input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n,m = map(int,input().split())
    data = deque()
    for i,j in enumerate(list(map(int,input().split()))):
        data.append((i,j))
    cnt = 0
    while True:
        num = data.popleft()
        flag = False
        for i in data:
            if i[1]>num[1]:
                data.append(num)
                flag = True
                break
        if not flag:
            cnt+=1
            if num[0]==m:
                print(cnt)
                break