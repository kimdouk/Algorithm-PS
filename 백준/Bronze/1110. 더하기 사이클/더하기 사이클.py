n=int(input())
i=0
final=n
while 1:
    a=n//10
    b=n%10
    c=a+b
    d=c%10
    n = (b*10)+d
    i+=1
    if final==n:
        break
print(i)