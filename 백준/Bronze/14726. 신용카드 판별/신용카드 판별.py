for _ in range(int(input())):
    number = list(map(int,input()))
    result = 0
    for i in range(len(number)-1,-1,-1):
        if i%2!=0:
            result+=number[i]
        else:
            number[i] = number[i]*2
            if number[i]>=10:
                number[i] = int(str(number[i])[0])+int(str(number[i])[1])
            result+=number[i]
    print('T' if result%10==0 else 'F')