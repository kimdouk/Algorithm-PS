from collections import deque
data = deque([i+1 for i in range(int(input()))])
result = []
while True:
    if len(data)==1:break
    result.append(data.popleft())
    data.append(data.popleft())
result.append(data.pop())
print(*result)