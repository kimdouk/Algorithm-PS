n = int(input())
row = [0] * n
result = 0
def isPossible(x):
    for i in range(x):
        if row[i]==row[x] or abs(x-i) == abs(row[x]-row[i]):
            return False
    return True
def n_queen(x):
    global result
    if x ==n:
        result +=1
        return
    for i in range(n):
        row[x] = i 
        if isPossible(x):
            n_queen(x+1)
n_queen(0)
print(result)