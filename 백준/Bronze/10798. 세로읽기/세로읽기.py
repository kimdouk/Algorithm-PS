data = []
mx = 0
for _ in range(5):
    string = list(input())
    mx = max(len(string),mx)
    data.append(string)
for i in range(5):
    if len(data[i])!=mx:
        for _ in range(mx-len(data[i])):
            data[i].append('')
for j in range(mx):
    for i in range(5):
        print(data[i][j],end='')