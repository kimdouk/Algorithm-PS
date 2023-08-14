n = input()[:-2]
f = int(input())
for i in range(0,100):
    if i<10:
        if int(n+'0'+str(i))%f==0:
            print('0'+str(i))
            break
    else:
        if (int(n+str(i)))%f==0:
            print(i)
            break