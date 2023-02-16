board = [list(map(int,input().split())) for _ in range(5)]
data = [list(map(int,input().split())) for _ in range(5)]
check = [[False]*5 for _ in range(5)]

def solve(findNum):
    count=0
    for i in range(5):
        for j in range(5):
            if board[i][j] == findNum:
                check[i][j] = True
    for i in range(5):
        if all(check[i]):
            count+=1
    for i in range(5):
        tmp=0
        for j in range(5):
            if check[j][i]:
                tmp+=1
        if tmp==5:
            count+=1
    tmp = 0
    for i in range(5):
        if check[i][i]:
            tmp+=1
    if tmp==5:
        count+=1
    tmp = 0
    for i in range(5):
        if check[i][4-i]:
            tmp+=1
    if tmp==5:
        count+=1

    if count>=3:    
        return True
    elif count<3:
        return False
result = 0
for i in range(5):
    for j in range(5):
        result +=1
        if solve(data[i][j]):
            print(result)
            exit()