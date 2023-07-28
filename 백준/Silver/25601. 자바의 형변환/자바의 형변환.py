input = __import__('sys').stdin.readline
dictionary = dict()
for _ in range(int(input())-1):
    child, parent = input().split()
    dictionary[child] = parent
def check(child,parent):
    while True:
        try:
            child = dictionary[child]
            if child == parent:return 1
        except:return 0

a,b = input().split()
print(check(a,b) or check(b,a))