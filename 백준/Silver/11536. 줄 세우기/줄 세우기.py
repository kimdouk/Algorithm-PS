n = int(input())
data = [input() for _ in range(n)]
if sorted(data) == data:print("INCREASING")
elif sorted(data, reverse=True) == data:print("DECREASING")
else:print("NEITHER")