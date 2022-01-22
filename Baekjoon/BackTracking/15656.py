n, m = map(int, input().split(' '))

num = list(map(int, input().split(' ')))
num.sort()

checked_list = [0] * n
num_arr = []


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    for i in range(n):
        num_arr.append(num[i])
        dfs(index + 1)
        num_arr.pop()


dfs(0)
