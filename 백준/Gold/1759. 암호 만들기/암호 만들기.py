import sys
sys.setrecursionlimit(10**6)
l,c = map(int,input().split())
alpha = sorted(list(input().split()))
vowel, consonant = 0,0
code = []
vowelCheck = ['a','i','e','o','u']
def backTrack(idx):
    global vowel
    global consonant
    if len(code) == l:
        if vowel>=1 and consonant>=2:
            print(''.join(code))
            return
    
    for i in range(idx,c):
        if alpha[i] in vowelCheck:vowel+=1
        else:consonant+=1
        code.append(alpha[i])
        backTrack(i+1)
        if code[-1] in vowelCheck:vowel-=1
        else:consonant-=1
        code.pop()
backTrack(0)