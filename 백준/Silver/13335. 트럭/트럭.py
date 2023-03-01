n, w, l = map(int,input().split())
train = list(map(int,input().split()))
bridge = [0] * w
result = 0
while bridge:
    bridge.pop(0)
    result +=1
    if len(train)!=0:
        if sum(bridge) + train[0] <=l:
            bridge.append(train.pop(0))
        else:
            bridge.append(0)
print(result)