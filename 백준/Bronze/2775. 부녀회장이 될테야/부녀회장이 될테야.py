for _ in range(int(input())):
    k = int(input())
    n = int(input())
    dp = [[0 for _ in range(14)] for j in range(15)]
    dp[0] = [i for i in range(1,15)]
    for i in range(1,15):
        for j in range(14):
            dp[i][j] += sum(dp[i-1][:j+1])
    print(dp[k][n-1])
    