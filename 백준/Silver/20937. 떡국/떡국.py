from collections import Counter
n = int(input())
print(Counter(list(map(int,input().split()))).most_common(1)[0][1])