from collections import defaultdict
def solution(answers):
    case1 = [1,2,3,4,5]
    case2 = [2,1,2,3,2,4,2,5]
    case3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = defaultdict(int)
    result = []
    for i in range(len(answers)):
        if case1[i%len(case1)]==answers[i]:
            cnt[1]+=1
        if case2[i%len(case2)]==answers[i]:
            cnt[2]+=1
        if case3[i%len(case3)]==answers[i]:
            cnt[3]+=1
    for i,j in sorted(cnt.items(), key=lambda x:x[0]):
        if max(cnt.values()) == j:
            result.append(i)
    return result
        
            