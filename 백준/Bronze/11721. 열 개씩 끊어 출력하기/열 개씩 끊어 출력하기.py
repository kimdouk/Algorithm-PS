s = input()
i = 0
for _ in range(len(s)//10+1):
    print(s[i:i+10])
    i+=10