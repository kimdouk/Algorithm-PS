from itertools import permutations
def solution(numbers):
    
    def check(num):
        for i in range(2,num):
            if num%i==0:return 0
        return 1
    # print(list(numbers))
    data = list(numbers)
    result = []
    cnt = 0
    for i in range(1,len(numbers)+1):
        for j in list(permutations(data,i)):
            tmp = ''.join(j)
            tmp = tmp.lstrip("0")
            if tmp!='' and tmp!='1':
                result.append(tmp)
    for num in set(result):
        cnt+=check(int(num))
    return cnt