from collections import deque, Counter
def bfs(v,dist,distance,graph,visited):
    distance[v] = dist
    queue = deque([(v,dist)])
    visited[v] = True
    while queue:
        x,dist = queue.popleft()
        distance[x] = dist
        for i in graph[x]:
            if not visited[i]:
                queue.append((i,dist+1))
                visited[i] = True
                
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] *(n+1)
    distance = [0] *(n+1)
    

    bfs(1,0,distance,graph,visited)  
    counter = Counter(distance)
    return (counter[max(distance)])
        
        
    