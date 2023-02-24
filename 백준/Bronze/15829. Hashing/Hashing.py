n = int(input())
string = input()
result = 0
for i in range(n):
    result += ((31**i )* (ord(string[i])-96))
print(result)