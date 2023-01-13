from collections import deque

def bfs(startNode):
    result = 0
    queue = deque([startNode])
    visited[startNode] = True

    while queue:
        result += 1
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

nodeNum = int(input())
edgeNum = int(input())
graph = [[] for _ in range(nodeNum + 1)]
for i in range(edgeNum):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [False] * (nodeNum+1)

print(bfs(1)-1)

# from collections import deque
# def bfs(graph, start, visited):
#     count = 0
#     queue = deque()
#     queue.append(start)
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         count+=1
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#     return count-1

# node = int(input())
# link = int(input())
# graph = [[] for _ in range(node+1)]
# for i in range(link):
#     v1, v2 = map(int,input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)
# visited = [False]*(node+1)

# print(bfs(graph,1,visited))