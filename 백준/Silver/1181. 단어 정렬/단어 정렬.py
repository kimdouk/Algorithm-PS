n = int(input())
data = [input() for _ in range(n)]
data = list(set(data))
data.sort(key=lambda x:(len(x),x))
print('\n'.join(data))