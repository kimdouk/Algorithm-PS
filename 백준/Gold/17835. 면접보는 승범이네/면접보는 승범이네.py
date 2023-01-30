#도시에서 면접장이 아니라 면접장에서 도시로 다익스트라를 돌려준다.(시간초과안나기위해)
#면접장을 모두 힙에 넣어줘도 다익스트라는 정상적으로 결과를 얻을 수 있음
#시작점이 여러곳이여도 된다.
import sys
import heapq

input = sys.stdin.readline
n, m, k= map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m): #역방향 그래프를 만들어준다.(면접장->도시 최단거리 게산을 위해)
    a,b,c = map(int,input().split())
    graph[b].append((a,c))
interviewPlace = list(map(int,input().split()))
INF = float('inf')
distance = [INF] * (n+1)

def dijkstra():
    q = []
    for place in interviewPlace:#시작점을 한번에 힙에 넣어준다.
        heapq.heappush(q, (0,place))
        distance[place] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nextNode, nextDist in graph[now]:
            cost = dist + nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost,nextNode))
    return distance[1:]

result = dijkstra()
print(result.index(max(result))+1, max(result), sep='\n')