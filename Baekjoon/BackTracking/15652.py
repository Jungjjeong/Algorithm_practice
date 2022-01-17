n, m = map(int, input().split(' '))

num_arr = []


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    for i in range(n):
        if index >= 1 and num_arr[index-1] > i+1:
            continue

        num_arr.append(i+1)
        dfs(index + 1)
        num_arr.pop()


dfs(0)
