import heapq
n = int(input())
data =[int(input()) for _ in range(n)]
heapq.heapify(data)
result = []
for _ in range(n-1):
    tmp = heapq.heappop(data)+heapq.heappop(data)
    result.append(tmp)
    heapq.heappush(data,tmp)
print(sum(result))