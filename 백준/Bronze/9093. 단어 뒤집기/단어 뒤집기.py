n = int(input())
for _ in range(n):
    data = input().split()
    for word in data:
        print(word[::-1],end=' ')
    print()