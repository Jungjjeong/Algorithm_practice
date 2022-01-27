n = int(input())

row = [0] * n
count = 0


def check(index):
    for i in range(index):
        if row[index] == row[i] or abs(row[index] - row[i]) == index - i:
            return False

    return True


def dfs(index):
    global count

    if index == n:
        count += 1
        return

    for i in range(n):
        row[index] = i
        if index == 0 or (index > 0 and check(index)):
            dfs(index + 1)


dfs(0)
print(count)
