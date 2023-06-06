n,m = map(int,input().split())
onePrice, packagePrice = [],[]
result = 0
for _ in range(m):
    package,one = map(int,input().split())
    onePrice.append(one)
    packagePrice.append(package)
onePrice.sort()
packagePrice.sort()
result += (n//6)*(min(onePrice[0]*6,packagePrice[0]))
result += min(onePrice[0]*(n%6),packagePrice[0])
print(result)