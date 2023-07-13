from itertools import permutations
num = [*permutations(range(1,10),3)]
for _ in range(int(input())):
    q,s,b = input().split()
    new_num = []
    while num:
        candidate = num.pop()
        temp_s, temp_b = 0,0 
        for i in range(3):
            for j in range(3):
                if i==j and candidate[i] == int(q[j]):temp_s+=1
                elif i!=j and candidate[i] == int(q[j]):temp_b+=1
        if int(s)==temp_s and int(b)==temp_b:
            new_num.append(candidate)
    num = new_num
print(len(num))