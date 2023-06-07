for _ in range(int(input())):
    h,w,n = map(int,input().split())
    floor,num = '',''
    if n%h==0:
        floor = str(h)
        num = n//h
    else:
        floor=str(n%h)
        num = n//h+1
    if num<10:num = '0'+str(num)
    print(floor+str(num))