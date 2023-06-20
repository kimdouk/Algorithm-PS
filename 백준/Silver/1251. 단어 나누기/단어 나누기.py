string = input()
result = []
for i in range(len(string)-2):
    for j in range(i+1,len(string)-1):
        result.append((string[:i+1])[::-1]+(string[i+1:j+1][::-1])+(string[j+1:][::-1]))
result.sort()
print(result[0])