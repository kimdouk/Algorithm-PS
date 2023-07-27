input = __import__('sys').stdin.readline
result = []
for _ in range(int(input())):
    a,d,g = map(int,input().split())
    score = a*(d+g)
    if a==(d+g):result.append(2*score)
    else:result.append(score)
print(sorted(result)[-1])