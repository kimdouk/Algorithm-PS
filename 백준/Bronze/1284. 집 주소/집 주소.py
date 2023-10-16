while True:
    n = input()
    if n=='0':break
    result = 0
    result+=len(n)+1
    for i in list(map(int,n)):
        if i==1:result+=2
        elif i==0:result+=4
        else:result+=3
    print(result)