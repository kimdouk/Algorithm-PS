name = input()
result = name[0]
for i in range(len(name)):
    if name[i]=='-':result+=name[i+1]
print(result)