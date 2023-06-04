from string import ascii_uppercase
find = list(ascii_uppercase)
while True:
    n,m = input().split("C")
    if n[1]=='0' and m=='0':break
    m = int(m)-1
    result = []
    while m>=0:
        result.append(find[m%26])
        m = (m//26) -1
    print(''.join(reversed(result))+n[1:])