from collections import deque
n = int(input())
q = deque([i+1 for i in range(n)])
for i in range(1,n):
    q.rotate(-(i**3-1))
    q.popleft()
print(q[0])