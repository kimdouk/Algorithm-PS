# # from collections import deque

# # def bfs(x,y,n,m,graph,visited):
# #     dx = [-1,1,0,0]
# #     dy = [0,0,-1,1]
    
# #     queue = deque([(x,y)])
# #     while queue:
# #         x,y = queue.popleft()
# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]
# #             if nx<0 or ny<0 or nx>=n or ny>=m:continue
# #             if graph[nx][ny] ==1 and not visited[nx][ny]:
# #                 visited[nx][ny] = True
# #                 queue.append((nx,ny))
                
# def dfs(x,y,n,m,graph,visited):
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
    
    
#     visited[x][y] = True
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or ny<0 or nx>=n or ny>=m:continue
#         if graph[nx][ny] ==1 and not visited[nx][ny]:
#             dfs(nx,ny,n,m,graph,visited)

# def solution(n, computers):
#     answer = 0
#     m = len(computers[0])
#     visited = [[False] *m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if computers[i][j] ==1 and not visited[i][j]:
#                 dfs(i,j,n,m,computers,visited)
#                 answer +=1
#     return answer

from collections import deque
def solution(n, computers):
    visited = [False for _ in range(n)]
    # dx,dy = [-1,1,0,0],[0,0,-1,1]
    def bfs(x):
        visited[x] = True
        q = deque([x])
        while q:
            x = q.popleft()
            for i in range(len(computers[x])):
                if not visited[i] and computers[x][i]:
                    q.append(i)
                    visited[i] = True
                    
        # visited[x][y] = True
        # q = deque([(x,y)])
        # for i in computers[x][y]:
        #     if
        # while q:
        #     x,y = q.popleft()
        #     for i in range(4):
        #         nx = x + dx[i]
        #         ny = y + dy[i]
        #         if nx<0 or ny<0 or nx>=n or ny>=n:continue
        #         if not visited[nx][ny] and computers[nx][ny]==1:
        #             q.append((nx,ny))
        #             visited[nx][ny] = True
                    
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt+=1
    return cnt