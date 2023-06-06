word = input()
search = input()
i, cnt = 0,0
while True:
    if i>len(word):
        break
    if search == word[i:i+len(search)]:
        cnt+=1
        i+=len(search)
    else:
        i+=1
print(cnt)