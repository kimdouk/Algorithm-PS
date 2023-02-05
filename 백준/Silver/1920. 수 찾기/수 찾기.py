def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

m = int(input())
array = sorted(list(map(int,input().split())))
n = int(input())
test = list(map(int,input().split()))

for i in range(n):
    result = binary_search(array, test[i], 0, m-1)
    if result == None:print(0)
    else:print(1)