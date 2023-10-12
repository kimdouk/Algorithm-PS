from collections import defaultdict
import math
def solution(fees, records):
    def check(st,end):
        time = 0
        time+= (int(end[:2])-int(st[:2]))*60
        minute = int(end[3:5])-int(st[3:5])
        time+=minute
        # if minute>=0:
        #     time+=minute
        # else:
        #     time+=minute
        return time
        
    recdict = defaultdict(list)
    for record in records:
        recdict[record[6:10]].append(record[:5])
    ans = []
    for i in sorted(list(recdict)):
        result = 0
        if len(recdict[i])%2==0:
            for j in range(0,len(recdict[i]),2):
                result += check(recdict[i][j],recdict[i][j+1])
        else:
            for j in range(0,len(recdict[i])-1,2):
                result += check(recdict[i][j],recdict[i][j+1])
            result += check(recdict[i][-1],'23:59')
        
        ans.append(fees[1] if result<=fees[0] else fees[1]+(math.ceil((result - fees[0])/fees[2]) * fees[3]))
    return ans