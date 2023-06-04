def next_permutations(string):
    k = -1
    for i in range(len(string)-1,0,-1):
        if string[i-1]< string[i]:
            k = i-1
            break
    if k==-1:return string
    
    for j in range(len(string)-1,-1,-1):
        if string[k]<string[j]:
            break
    
    string[k],string[j] = string[j],string[k]
    result = string[:k+1]
    result.extend(reversed(string[k+1:]))
    return result

for _ in range(int(input())):
    string = list(input())
    print(''.join(next_permutations(string)))