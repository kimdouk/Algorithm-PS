n = int(input())
buildings = [int(input()) for _ in range(n)]
stack = [buildings[0]]
result = 0
for i in range(1,n):
    while stack and buildings[i] >= stack[-1]:
        stack.pop()
    stack.append(buildings[i])
    result += (len(stack)-1)
print(result)