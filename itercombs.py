from itertools import combinations
import math
word = input("")
sorted_list = sorted(word.split()[0])
word1 = "".join(sorted_list)
k = int(word.split()[1])
allcombs = {}
alllists = {}

for t in range(k):
    allcombs[f'comb{t+1}'] = combinations(word1, t+1)
    alllists[f'list1{t+1}'] = list(combinations(word1, t+1))
    
n = int(math.factorial(len(word1))/(math.factorial(k)*math.factorial(len(word1) - k)))
print(alllists)
for i in range(k):
    for l in range(len(alllists[f'list1{i+1}'])):
        print("".join(alllists[f'list1{i+1}'][l]))

