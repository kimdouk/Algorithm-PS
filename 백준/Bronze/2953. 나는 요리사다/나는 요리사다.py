data = [sum(list(map(int,input().split()))) for _ in range(5)]
print(data.index(max(data))+1, max(data))