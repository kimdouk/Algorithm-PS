n,k = map(int,input().split())
data = list(map(int,input().split()))
def is_odd(x): #홀수판별
    if x%2!=0:return True

odd,even = 0,0
end,result = 0,0
for start in range(n):
    while end<n and odd<=k:
        if is_odd(data[end]):odd+=1 #홀수일경우 홀수+=1
        else:even+=1 #짝수일경우 짝수+=1
        end+=1
        if end==n:#범위넘어가면
            result = max(result,even)#지금까지 짝수최대길이 저장
            break
    if odd==k+1:#홀수가 k+1번째가 될떄(중요)
        result = max(result,even)#지금까지 짝수최대길이 저장
    if is_odd(data[start]):odd-=1#start이동 전, 홀수면 홀수-=1
    elif not is_odd(data[start]):even-=1#짝수면 짝수-=1
print(result)