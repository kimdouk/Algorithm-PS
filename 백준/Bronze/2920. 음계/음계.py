data = [*map(int,input().split())]
ans = [1,2,3,4,5,6,7,8]
if data==ans:print("ascending")
elif data==sorted(ans, reverse=True):print("descending")
else:print("mixed")