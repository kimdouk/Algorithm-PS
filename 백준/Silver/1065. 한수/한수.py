n=int(input())
hansu = 0
if len(str(n))<3:
    hansu=n
else:
    hansu=99
    for i in range(100,n+1):
        if int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0]):
            hansu+=1
print(hansu)