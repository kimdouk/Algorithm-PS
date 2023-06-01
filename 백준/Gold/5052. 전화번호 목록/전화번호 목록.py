import sys
input = sys.stdin.readline
def isCheck(number1,number2):
    if number1 == number2[:len(number1)]:
        return True
    else: return False

for _ in range(int(input())):
    n = int(input())
    number = sorted([input().strip() for _ in range(n)])
    result = 'YES'
    for i in range(n-1):
        if isCheck(number[i],number[i+1]):
            result = 'NO'
            break
    print(result)