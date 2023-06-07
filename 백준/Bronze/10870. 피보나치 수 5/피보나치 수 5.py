f = [0,1]
for i in range(2,21):
    f.append(f[i-1]+f[i-2])
print(f[int(input())])