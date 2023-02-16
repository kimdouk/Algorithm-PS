import itertools
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
cardDeck = [int(input()) for _ in range(n)]
kDeck = list(itertools.combinations(cardDeck,k))
result = set()
for i in kDeck:
  numList = list(itertools.permutations(i,k))
  for num in numList:
    result.add(int(''.join(map(str,num))))
print(len(result))