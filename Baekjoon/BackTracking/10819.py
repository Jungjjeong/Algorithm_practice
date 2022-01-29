from itertools import permutations as per

n = int(input())

n_list = list(map(int, input().split(' ')))
per_list = list(per(n_list, n))

result = 0

for p in per_list:
    max_temp = 0
    for i in range(n-1):
        max_temp += abs(p[i]-p[i+1])
    if result < max_temp:
        result = max_temp

print(result)
