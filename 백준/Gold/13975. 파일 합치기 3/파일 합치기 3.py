import heapq
t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int,input().split()))
    data = []
    for i in a:
        heapq.heappush(data,i)
    sm = 0
    while True:
        temp = heapq.heappop(data)+heapq.heappop(data)
        sm += temp
        heapq.heappush(data,temp)
        if len(data) == 1:
            break
    print(sm)