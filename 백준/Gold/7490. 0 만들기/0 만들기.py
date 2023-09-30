def check():
    num_op = [data[0]]
    for i in range(len(operator)):
        num_op.append(operator[i])
        num_op.append(data[i+1])
    temp = []
    for j in range(len(num_op)):
        if num_op[j-1]==' ':continue
        if num_op[j]==' ':
            t = temp.pop()
            temp.append(int(str(t)+str(num_op[j+1])))
        else:temp.append(num_op[j])
    total=temp[0]
    for i in range(1,len(temp),2):
        if temp[i]=='+':
            total+=temp[i+1]
        else:total-=temp[i+1]
    if total==0:
        result.append(num_op)

def dfs():
    if len(operator)==len(data)-1:
        check()
        return
    
    for i in [' ','+','-']:
        operator.append(i)
        dfs()
        operator.pop()

for _ in range(int(input())):
    data = [i for i in range(1,int(input())+1)]
    operator = []
    result = []
    dfs()
    for ans in result:
        print(*ans,sep='')
    print()