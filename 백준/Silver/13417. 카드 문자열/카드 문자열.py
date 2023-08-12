from collections import deque
input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().split()
    q = deque([s[0]])
    for alpha in s[1:]:
        if ord(alpha)>ord(q[0]):q.append(alpha)
        else:q.appendleft(alpha)
    print(''.join(q))