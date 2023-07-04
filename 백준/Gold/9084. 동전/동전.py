for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    m = int(input())
    dp = [1] + [0 for _ in range(m)]

    for coin in coins:
        for i in range(coin,m+1):
            dp[i] = dp[i] + dp[i-coin]
    print(dp[-1])