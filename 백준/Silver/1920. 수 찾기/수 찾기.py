def binary_search(array,target,start,end):
    while start<=end:
        mid = (start + end)//2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
array = sorted(list(map(int,input().split())))
m = int(input())
data = list(map(int,input().split()))

for target in data:
    print(binary_search(array,target,0,n-1))