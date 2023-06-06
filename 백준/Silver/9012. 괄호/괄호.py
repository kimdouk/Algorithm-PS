for _ in range(int(input())):
    string = input()
    stack = []
    flag = 0
    for i in string:
        if i =='(':
            stack.append(i)
        else:
            if len(stack)==0:
                print('NO')
                flag = 1
                break
            stack.pop()
    if not flag:
        if len(stack)==0:
            print("YES")
        else:print('NO')