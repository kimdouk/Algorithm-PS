def solution(progresses, speeds):
    result = []
    time = 0
    while True:
        if sum(progresses)==-1*(len(progresses)):break
        for i in range(len(progresses)):
            if progresses[i]!=-1:
                progresses[i] +=speeds[i]
            if progresses[i]>=100:
                progresses[i] = -1
        cnt = 0
        if progresses[time]==-1:
            for i in range(time, len(progresses)):
                if progresses[i]==-1:
                    cnt+=1
                else:
                    time = i
                    break
            result.append(cnt)
    return result
                
        