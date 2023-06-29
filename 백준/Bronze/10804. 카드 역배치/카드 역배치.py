deck = [i for i in range(21)]
for _ in range(10):
    a,b = map(int,input().split())
    tmp = deck[a:b+1]
    deck[a:b+1] = tmp[::-1]
print(*deck[1:])