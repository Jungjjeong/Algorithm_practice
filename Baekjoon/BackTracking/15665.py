n, m = map(int, input().split(' '))

num = list(map(int, input().split(' ')))
num.sort()

num_arr = []


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    before_num = 0

    for i in range(n):
        if num[i] != before_num:
            num_arr.append(num[i])
            before_num = num[i]
            dfs(index + 1)
            num_arr.pop()


dfs(0)
