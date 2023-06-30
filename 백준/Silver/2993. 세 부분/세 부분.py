word = input()
result = []
for i in range(len(word)-2):
    wordcpy = word
    for j in range(i+1,len(word)-1):
        result.append(wordcpy[:i+1][::-1]+wordcpy[i+1:j+1][::-1]+wordcpy[j+1:][::-1])
result.sort()
print(result[0])