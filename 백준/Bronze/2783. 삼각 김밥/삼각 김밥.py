x,y = map(int,input().split())
price = [x/y]
for _ in range(int(input())):
    x,y = map(int,input().split())
    price.append(x/y)
price.sort()
print(price[0]*1000)