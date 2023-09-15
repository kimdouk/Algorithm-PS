from bisect import bisect_left
def solution(citations):
    citations.sort()
    for i in range(citations[-1],-1,-1):
        num = len(citations[bisect_left(citations,i):])
        if i<=num:
            return i
        
        
