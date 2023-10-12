cnt, flag, result = 0,0,0
def solution(word):
    def dfs(string):
        global cnt; global flag; global result
        if string == word:
            flag = 1
            result = cnt
            return 
        if len(string)==5:
            return

        for char in ['A', 'E', 'I', 'O', 'U']:
            if flag==1:return
            cnt+=1
            dfs(string+char)
        return
    
    dfs('')
    return result