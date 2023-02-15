import sys
sys.setrecursionlimit(10**6)
n = int(input())
s = [0]*n
w = [0]*n
for i in range(n):
    s[i], w[i] = map(int,input().split())
result = 0

def backTrack(idx,s_eggs):
    global result
    if idx ==n:
        count = 0
        for i in range(n):
            if s_eggs[i]<=0:count+=1
        result = max(result,count)#깰수있는 달걀의 최대 개수
        return
    
    if s_eggs[idx]<=0:backTrack(idx+1,s_eggs) #잡은달걀이 깨진달걀일경우 다음달걀 잡기(칠 수가 없는경우)
    else:
        check = False
        for i in range(n):
            if i!=idx and s_eggs[i]>0:#잡은달걀로 치려는 달걀이 꺠지지 않았을 때#자기자신제외
                check = True #칠 수 있는 달걀이 있다!
                temp_eggs = s_eggs[:]
                temp_eggs[i]-=w[idx]
                temp_eggs[idx]-=w[i]
                backTrack(idx+1, temp_eggs)
        if not check: #달걀이 모두 깨져있을 때(칠 달걀이 없는경우)
            backTrack(idx+1, s_eggs)#다음달걀 잡기
backTrack(0,s)
print(result)