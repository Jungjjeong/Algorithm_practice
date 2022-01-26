from itertools import combinations

n, s = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))

count = 0

for i in range(1, n + 1):
    combi_list = list(combinations(num_list, i))
    for c in combi_list:
        if sum(c) == s:
            count += 1

print(count)
