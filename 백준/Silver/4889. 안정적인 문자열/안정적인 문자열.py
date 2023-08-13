input = __import__('sys').stdin.readline
num = 0
while True:
    stack = []
    string = input()
    if string.startswith('-'):break
    cnt = 0
    num+=1
    for char in string:
        if not stack:
            if char == '}':
                cnt+=1
                stack.append('{')
            else:stack.append(char)
        else:
            if char =='}' and stack[-1]=='{':
                stack.pop()
            else:stack.append(char)
    cnt+=(len(stack)//2)
    print(str(num)+'.',cnt)