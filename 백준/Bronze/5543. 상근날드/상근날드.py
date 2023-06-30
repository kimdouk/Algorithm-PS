hamburger = [int(input()) for _ in range(3)]
coke = [int(input()) for _ in range(2)]
result = []
for i in hamburger:
    for j in coke:
        result.append(i+j-50)
result.sort()
print(result[0])