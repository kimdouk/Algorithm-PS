s = input()
t = list(input())
result = 0
while t:
    if ''.join(t) ==s:
        result = 1
        break
    if t[-1]=='A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]
print(result)