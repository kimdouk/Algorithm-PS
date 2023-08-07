n = int(input())
data = list(map(int,input().split()))[::-1]
stack = []
result = []
for num in data:
    if stack and num<stack[-1]:
        result.append(stack[-1])
        stack.append(num)
    else:
        while stack:
            if num>=stack[-1]:
                stack.pop()
            else:
                result.append(stack[-1])
                stack.append(num)
                break
    if not stack:
        result.append(-1)
        stack.append(num)
print(*result[::-1])