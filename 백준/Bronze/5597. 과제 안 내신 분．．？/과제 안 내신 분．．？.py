import sys
input = sys.stdin.readline
student = [0] * (30)
for i in range(28):
    student[int(input())-1] = 1
for i in range(30):
    if student[i] ==0:
        print(i+1)