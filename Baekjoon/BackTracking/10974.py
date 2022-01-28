n = int(input())

check = [0] * n
num_arr = []

def dfs(index):
    if index == n:
        print(*num_arr)
        return

    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            num_arr.append(i + 1)
            dfs(index + 1)
            check[i] = 0
            num_arr.pop()


dfs(0)