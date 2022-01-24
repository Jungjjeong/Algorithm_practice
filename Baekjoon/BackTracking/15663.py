n, m = map(int, input().split(' '))

num = list(map(int, input().split(' ')))
num.sort()

num_arr = []
checked_list = [0] * n


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    before_num = 0

    for i in range(n):
        if checked_list[i] == 0 and num[i] != before_num:
            checked_list[i] = 1
            num_arr.append(num[i])
            before_num = num[i]
            dfs(index + 1)
            checked_list[i] = 0
            num_arr.pop()


dfs(0)
