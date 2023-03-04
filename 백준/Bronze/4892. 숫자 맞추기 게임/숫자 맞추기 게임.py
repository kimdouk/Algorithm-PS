i = 0
while True:
    n = int(input())
    if n!=0:
        i+=1
        if (n*3)%2==0:print(str(i)+'.','even',(((round((3*n)//2,0))*3)//9))
        else:print(str(i)+'.','odd',(((round((3*n)//2,0))*3)//9))
    else:break