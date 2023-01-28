s = input()
data=[]
for i in range(len(s)):
    data.append(s[i:])
print('\n'.join(sorted(data)))