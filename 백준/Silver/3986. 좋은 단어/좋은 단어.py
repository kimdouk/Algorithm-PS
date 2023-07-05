cnt = 0
for _ in range(int(input())):
    flag = 0
    stack = []
    for alpha in input():
        if stack and stack[-1]==alpha:
            stack.pop()
        else:
            stack.append(alpha)
    if not stack:
        cnt+=1
print(cnt)