n, m = map(int, input().split(' '))

num = list(map(int, input().split(' ')))
num.sort()

num_arr = []
checked_list = [0] * n


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    for i in range(n):
        if index >= 1 and num_arr[index-1] > num[i]:
            continue

        num_arr.append(num[i])
        dfs(index + 1)
        num_arr.pop()


dfs(0)
