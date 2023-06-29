a = []
for _ in range(7):
    num = int(input())
    if num%2!=0:
        a.append(num)
if not a:print(-1)
else:print(sum(a),min(a),sep='\n')