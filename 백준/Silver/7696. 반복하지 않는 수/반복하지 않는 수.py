from itertools import permutations,chain,islice
from math import perm

def make_num(len):
    len_iter = permutations(range(10),len)
    return islice(len_iter, perm(9,len-1), None)
while True:
    n = int(input())
    if n==0:break
    result = chain(*map(make_num,range(1,11)))
    print(''.join(map(str,next(islice(result,n-1,None)))))