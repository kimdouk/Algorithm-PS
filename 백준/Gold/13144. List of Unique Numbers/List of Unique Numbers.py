n = int(input())
data = list(map(int,input().split()))
check = [0]*(max(data)+1)
end = 0
result = 0
for start in range(n):
    while end<n:
        if check[data[end]] == True:
            break
        check[data[end]] = True
        end+=1

    result += (end-start)
    check[data[start]] = False
print(result)