def check(data):
    #check1
    cnt = 0
    for i in data:
        if i in ['a','e','i','o','u']:
            cnt+=1
    if cnt==0:return False
    # check2
    
    for i in range(len(data)-2):
        cnt2=0
        for j in range(3):
            if data[i+j] in ['a','e','i','o','u']:
                cnt2+=1
        if cnt2==0 or cnt2==3:return False
    #check3
    for i in range(len(data)-1):
        if data[i]=='e' or data[i]=='o':continue
        if data[i]==data[i+1]:return False
    return True

while True:
    string = input()
    if string=='end':break
    if check(string):print('<'+string+'> is acceptable.')
    else: print('<'+string+'> is not acceptable.')