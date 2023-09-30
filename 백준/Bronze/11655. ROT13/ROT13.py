data = input()
result = ''
for c in data:
    if c.isupper():
        if ord(c)+13>90:
            result+=chr(64+(ord(c)+13)%90)
        else:result+=chr(ord(c)+13)
    elif c.islower():
        if ord(c)+13>122:
            result+=chr(96+(ord(c)+13)%122)
        else:result+=chr(ord(c)+13)
    else:result+=c
print(result)