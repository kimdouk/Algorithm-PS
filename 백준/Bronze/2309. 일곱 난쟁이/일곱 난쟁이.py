from itertools import combinations
length = []
for _ in range(9):
    length.append(int(input()))
for i in list(combinations(length, 7)):
    if sum(i)==100:
        print(*sorted(i),sep='\n')
        break