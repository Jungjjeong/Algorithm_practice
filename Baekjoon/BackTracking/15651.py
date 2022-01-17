n, m = map(int, input().split(' '))

num_arr = []


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    for i in range(n):
        num_arr.append(i+1)
        dfs(index + 1)
        del num_arr[index]


dfs(0)
