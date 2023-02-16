from itertools import product
n,k = map(int,input().split())
data = list(map(int,input().split()))
length = len(str(n))
result = []
while True:
  for i in list(product(data,repeat = length)):
    num = int(''.join(map(str,i)))
    if num<=n:
      result.append(num)
  if len(result)>0:
    print(max(result))
    break
  else:
    length-=1