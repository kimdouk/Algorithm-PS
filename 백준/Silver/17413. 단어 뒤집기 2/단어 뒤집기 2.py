data = input()
i=0
result = ''
start = 0
flag = 0
while True:
    
    if data[i] =='<':
        start = i
        while True:
            i+=1
            if data[i] =='>':
                result+=(data[start:i+1])
                if i+1==len(data):
                    flag =1
                    break
                else:
                    i+=1
                    break

    else:
        start = i
        while True:
            i+=1
            if i == len(data):
                temp = data[start:i].split()
                for j in temp:
                    result+=j[::-1]+' '
                result = result[:-1]
                flag =1
                break
            if data[i] =='<':
                temp = data[start:i].split()
                for j in temp:
                    result+=j[::-1]+' '
                result = result[:-1]
                    
                break
    if flag == 1:break
print(result)