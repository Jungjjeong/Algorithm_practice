n = int(input())
n_list = [1]


def dfs(index):
    global min_num

    for j in range(1, (index + 1)//2 + 1):
        if n_list[-j:] == n_list[-2*j:-j]:
            return

    if index == n - 1:
        print(''.join(map(str, n_list)))
        return -1

    for i in range(1, 4):
        if n_list[index] == i:
            continue

        n_list.append(i)
        if dfs(index + 1) == -1:
            return -1
        n_list.pop()


dfs(0)
