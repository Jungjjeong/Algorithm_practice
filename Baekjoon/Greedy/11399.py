from time import time


num = int(input())
time_arr = list(map(int, input().split(' ')))

time_arr = sorted(time_arr)

sum = 0
sum_num = 1

for n in range(num):
    for s in range(sum_num):
        sum += time_arr[s]
    sum_num += 1

print(sum)
