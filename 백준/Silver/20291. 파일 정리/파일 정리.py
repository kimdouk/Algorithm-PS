import sys
input = sys.stdin.readline
n = int(input())
fileDict ={}
for _ in range(n):
    file = input().split('.')[1]
    if file not in fileDict:
        fileDict[file] = 1
    else:
        fileDict[file] += 1
fileDict = sorted(fileDict.items())
for key, value in fileDict:
    print(key.strip(),value)