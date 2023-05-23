# 시간초과
# import sys
# input = sys.stdin.readline
# s1 = input().strip()
# s2 = input().strip()
# dp = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]
# result_str = ''
# std_i, std_j = 0,0
# for i in range(1,len(s1)+1):
#     for j in range(1,len(s2)+1):
#         if s1[i-1] == s2[j-1]:
#             dp[i][j] = dp[i-1][j-1]+s1[i-1]
#         else:
#             if len(dp[i-1][j])>=len(dp[i][j-1]):
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i][j-1]
# print(len(dp[-1][-1]), dp[-1][-1], sep='\n')


s1 = input()
s2 = input()
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
result = ''
i,j = len(s1), len(s2)
while i>0 and j>0:
    if dp[i][j-1] == dp[i][j]:j-=1
    elif dp[i-1][j] == dp[i][j]:i-=1
    else:
        result+=s1[i-1]
        i-=1
        j-=1
print(dp[-1][-1], result[::-1], sep='\n')