from bisect import bisect_right,bisect_left
def count_by_range(left,right):
    left_idx = bisect_left(array, left)
    right_idx = bisect_right(array, right)
    return right_idx - left_idx

n = int(input())
array = sorted(list(map(int,input().split())))
m = int(input())
test = list(map(int,input().split()))

result = []
for i in range(m):
    result.append(count_by_range(test[i],test[i]))
print(*result)
