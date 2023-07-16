price = sorted([int(input()) for _ in range(int(input()))], reverse=True)
result = 0
for i in range(0,len(price),3):
    if i==((len(price)//3)*3):result+=sum(price[i:])
    else:result+=sum(price[i:i+2])
print(result)