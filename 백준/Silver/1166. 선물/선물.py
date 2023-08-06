input = __import__('sys').stdin.readline
n,l,w,h = map(int,input().split())
st,end = 0,min(l,w,h)
for _ in range(1000):
    mid = (st+end)/2
    if (l//mid)*(w//mid)*(h//mid)>=n:
        result = mid
        st = mid
    else:end = mid
print('%.10f'%result)