from collections import defaultdict
bookDict = defaultdict(int)
for _ in range(int(input())):
    book = input()
    bookDict[book]+=1
bookDict = sorted(bookDict.items(), key=lambda x:(-x[1],x[0]))
print(bookDict[0][0])