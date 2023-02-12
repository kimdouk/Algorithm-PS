n,k = map(int,input().split())
data = list(map(int,input().split()))
def is_odd(x):
    if x%2!=0:return True

odd,even = 0,0
end,result = 0,0
for start in range(n):
    while end<n and odd<=k:
        if is_odd(data[end]):odd+=1
        else:even+=1
        end+=1
        if end==n:
            result = max(result,even)
            break
    if odd==k+1:
        result = max(result,even)
    if is_odd(data[start]):odd-=1
    elif not is_odd(data[start]):even-=1
print(result)