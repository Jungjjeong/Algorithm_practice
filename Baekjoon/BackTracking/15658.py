from itertools import permutations as per
from itertools import combinations as com
import sys


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split(' ')))
operator_input_list = list(map(int, sys.stdin.readline().split(' ')))

operator_list = []

for i in range(4):
    if operator_input_list[i] > 0:
        for _ in range(operator_input_list[i]):
            operator_list.append(i)

com_n_list = list(com(n_list, n))
per_o_list = list(per(operator_list, n-1))
print(per_o_list)

max = float('-inf')
min = float('inf')

for cn in com_n_list:
    for po in per_o_list:
        temp = cn[0]
        for i in range(n-1):
            if po[i] == 0:
                temp += cn[i+1]
            elif po[i] == 1:
                temp -= cn[i+1]
            elif po[i] == 2:
                temp *= cn[i+1]
            elif po[i] == 3:
                if temp < 0:
                    temp = -(abs(temp) // cn[i+1])
                else:
                    temp //= cn[i+1]
        if temp > max:
            max = temp
        if temp < min:
            min = temp

print(max)
print(min)
