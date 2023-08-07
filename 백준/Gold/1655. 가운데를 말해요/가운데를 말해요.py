import heapq
input = __import__('sys').stdin.readline
n = int(input())
max_heap, min_heap = [], []
for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-num)
    else:heapq.heappush(min_heap,num)
    if min_heap and (-max_heap[0]>min_heap[0] ):
        mx = -heapq.heappop(max_heap)
        mn = heapq.heappop(min_heap)
        heapq.heappush(max_heap,-mn)
        heapq.heappush(min_heap,mx)
    
    print(-max_heap[0])