import math
num = list(map(int,input().split(':')))
gcd = math.gcd(num[0],num[1])
print(str(num[0]//gcd)+':'+str(num[1]//gcd))