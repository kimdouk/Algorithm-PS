from math import sqrt
for _ in range(int(input())):
    secret = []
    string = input()
    n = int(sqrt(len(string)))
    for i in range(n):
        secret.append(list(string[i*n:(i+1)*n]))
    answer = []
    for j in range(len(secret)-1,-1,-1):
        for i in range(len(secret)):
            answer.append(secret[i][j])
    print(''.join(answer))