n = int(input())
flag = 0
num = 1
stack = []
result = []
for _ in range(n):
    target = int(input())
    while num<=target:
        stack.append(num)
        result.append('+')
        num+=1
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        flag = 1
print('\n'.join(result) if flag ==0 else 'NO')