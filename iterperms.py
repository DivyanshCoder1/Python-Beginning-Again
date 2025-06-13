from itertools import permutations
import math

word = str(input())
sorted_list = sorted(word.split()[0])
k = int(word.split()[1])
word1 = "".join(sorted_list)
perms = permutations(word1, k)
list1 = list(perms)
n = int(math.factorial(len(word1))/math.factorial(len(word1) - k))
print
for i in range(n):
    print("".join(list1[i]))