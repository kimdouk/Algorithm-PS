import heapq
input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    heapq.heapify(data)
    ans = 1
    while len(data)>=2:
        a = heapq.heappop(data)
        b = heapq.heappop(data)
        ans *=(a*b)
        heapq.heappush(data,a*b)
    print(ans%1000000007)