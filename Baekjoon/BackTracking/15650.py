n, m = map(int, input().split(' '))

checked_list = [0] * n
num_arr = []


def dfs(index):
    if index == m:
        print(*num_arr)
        return

    for i in range(n):
        if index >= 1 and num_arr[index-1] >= i+1:
            continue
        if checked_list[i] == 0:
            checked_list[i] = 1
            num_arr.append(i+1)
            dfs(index + 1)
            num_arr.remove(i+1)
            checked_list[i] = 0


dfs(0)
