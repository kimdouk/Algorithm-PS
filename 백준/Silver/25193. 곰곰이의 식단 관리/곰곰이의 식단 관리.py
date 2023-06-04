import math
n = int(input())
food = list(input())
elseFoodCnt = 1
chickenCnt = food.count("C")
elseFoodCnt += (n-chickenCnt)
print(math.ceil(chickenCnt/elseFoodCnt))