import string
move = {"R":(0,1),"L":(0,-1),"B":(-1,0),"T":(1,0),"RT":(1,1),"LT":(1,-1),"RB":(-1,1),"LB":(-1,-1)}
king,stone,n = input().split()
alpha = string.ascii_uppercase
king_space = [int(king[1]),alpha.index(king[0])+1]
stone_space = [int(stone[1]),alpha.index(stone[0])+1]

for _ in range(int(n)):
    moveto = move[input()]
    nx = king_space[0] + moveto[0]
    ny = king_space[1] + moveto[1]
    if nx<1 or ny<1 or nx>8 or ny>8:continue
    if nx == stone_space[0] and ny == stone_space[1]:
        nsx,nsy = stone_space[0]+moveto[0], stone_space[1]+moveto[1]
        if nsx<1 or nsy<1 or nsx>8 or nsy>8:continue
        king_space[0], king_space[1] = nx,ny
        stone_space[0], stone_space[1] = nsx,nsy
    else:
        king_space[0], king_space[1] = nx,ny

print(alpha[king_space[1]-1]+str(king_space[0]), alpha[stone_space[1]-1]+str(stone_space[0]), sep='\n')