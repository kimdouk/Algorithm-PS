result = 0
def solution(numbers, target):
    
    def dfs(depth, total):
        global result
        if depth>=len(numbers):
            if total == target:
                result +=1
            return
        
        
        
        total += numbers[depth]
        dfs(depth+1,total)
        total -= (numbers[depth]*2)
        dfs(depth+1,total)
            
    dfs(0,0)
    return result

