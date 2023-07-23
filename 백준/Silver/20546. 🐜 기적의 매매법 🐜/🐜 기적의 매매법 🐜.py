money = int(input())
cost = list(map(int,input().split()))
jmoney,smoney = money,money
jcnt,scnt = 0,0
for i in range(len(cost)):
    if cost[i]<=jmoney:
        jcnt += jmoney//cost[i]
        jmoney%=cost[i]
jh = jmoney+(jcnt*cost[-1])

for i in range(3,len(cost)):
    if len(set(cost[i-3:i])) != len(cost[i-3:i]):continue
    if cost[i-3:i] == sorted(cost[i-3:i]):
        smoney += scnt*cost[i]
        scnt = 0
    elif cost[i-3:i] == sorted(cost[i-3:i], reverse=True):
        scnt += smoney//cost[i]
        smoney%=cost[i]
sh = smoney+(scnt*cost[-1])
if jh>sh:print("BNP")
elif jh<sh:print("TIMING")
else:print("SAMESAME")