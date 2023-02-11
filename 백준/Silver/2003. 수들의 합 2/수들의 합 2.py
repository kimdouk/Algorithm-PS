n, m = map(int,input().split())
array = list(map(int,input().split()))
end = 0
total = array[0]
result = 0
for start in range(n):
    while end < n and total < m:
        end += 1
        if end != n:
            total += array[end]
    if total == m: result+=1
    if end == n: break
    total -= array[start]
print(result)