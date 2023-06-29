a,b = map(int,input().split())
a,b = min(a,b), max(a,b)
arr = [i for i in range(a+1,b)]
print(len(arr))
print(*arr)