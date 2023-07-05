while True:
    string = input()
    if string =='.':break
    stack = []
    flag = 0
    for char in string:
        if char in ('[','('):
            stack.append(char)
        elif char in (']',')'):
            if not stack:
                flag = 1
                break
            if char ==']':
                if stack.pop() != '[':
                    flag = 1
                    break
            elif char ==')':
                if stack.pop() !='(':
                    flag = 1
                    break
    if not stack and not flag:
        print('yes')
    else:print('no')