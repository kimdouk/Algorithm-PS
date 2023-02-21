from collections import deque
n = int(input())
card = [i for i in range(1,n+1)]
queue = deque(card)
while len(queue)>1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(queue.popleft())