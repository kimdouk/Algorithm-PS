a,b,c = map(int,input().split())

def dfs(num):
    if num==1:
        return a%c
    else:
        temp = dfs(num//2)
        if num%2==0:
            return (temp*temp) %c
        else:
            return (temp*temp*a)%c
print(dfs(b))