from collections import defaultdict
import sys
input = sys.stdin.readline
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self,string):
        curr_node = self.root
        flag = 0
        for i in range(len(string)):
            if string[i] not in curr_node:
                curr_node[string[i]] = {}
                if flag==0:
                    print(string[:i+1])
                    flag = 1
            curr_node = curr_node[string[i]]
        curr_node["*"] = string
    def search(self,string):
        curr_node = self.root
        for char in string:
            if char in curr_node:
                curr_node = curr_node[char]
            else:return False
        return True
trie = Trie()
cntdict = defaultdict(int)
for _ in range(int(input())):
    string = input().strip()
    if trie.search(string):
        cntdict[string]+=1
        if cntdict[string]>1:
            print(string+str(cntdict[string]))
        else:print(string)
    else:
        trie.insert(string)
        cntdict[string]+=1