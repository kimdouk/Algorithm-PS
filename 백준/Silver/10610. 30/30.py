n = list(map(int,input()))
if 0 not in n:
    print(-1)
else:
    if sum(n)%3==0:
        n.sort(reverse=True)
        print(''.join(map(str,n)))
    else:print(-1)