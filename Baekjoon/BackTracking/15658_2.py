from itertools import combinations as com


n = int(input())
n_list = list(map(int, input().split(' ')))
o_list = list(map(int, input().split(' ')))
o_append_list = []

for i in range(4):
    if o_list[i] > 0:
        for j in range(o_list[i]):
            o_append_list.append(i)


check_list = [0] * n
result = []

com_o_list = list(com(o_append_list, n-1))

max = -float('inf')
min = float('inf')


def dfs(index):
    global min, max

    if index == n:
        for c in com_o_list:
            temp = result[0]
            for i in range(n - 1):
                if c[i] == 0:
                    temp += result[i + 1]
                elif c[i] == 1:
                    temp -= result[i + 1]
                elif c[i] == 2:
                    temp *= result[i+1]
                elif c[i] == 3:
                    if temp < 0:
                        temp = -(-temp // result[i+1])
                    else:
                        temp //= result[i+1]
            if temp > max:
                max = temp
            if temp < min:
                min = temp
        return

    for i in range(n):
        if check_list[i] == 0:
            result.append(n_list[i])
            check_list[i] = 1
            dfs(index + 1)
            result.pop()
            check_list[i] = 0


dfs(0)
print(max, min)
