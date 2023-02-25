def solution(n, times):
    start, end = 0,max(times)*n
    while start<=end:
        count = 0
        mid = (start+end)//2
        for time in times:
            if time<=mid:
                count += (mid//time)
        if count>=n:
            result = mid
            end = mid-1
        else:
            start = mid +1
    return result
            