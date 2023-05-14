import sys

wait_dict = dict()
k, l = map(int,input().split())
for i in range(l):
    wait_dict[sys.stdin.readline().strip()] = i
wait_list = list(wait_dict.items())
wait_list = sorted(wait_list, key = lambda x:x[1])

if k>len(wait_list):
    for i in wait_list:
        print(i[0])
else:
    for i in range(k):
        print(wait_list[i][0])