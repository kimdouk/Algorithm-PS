# a+b+c = d는 a+b=d-c와 같다.
#입력(dataSet)은 집합이고 좌항(leftSide)도 중복이 의미가 없다.
import sys
input = sys.stdin.readline
n = int(input())
dataSet = set(int(input()) for _ in range(n))
leftside = set()
result = []
for a in dataSet:
    for b in dataSet:
        leftside.add(a+b)
for c in dataSet:
    for d in dataSet:
        if (d-c) in leftside:
            result.append(d)
print(sorted(result)[-1])