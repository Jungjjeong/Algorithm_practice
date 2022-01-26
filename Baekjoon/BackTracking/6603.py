lotto = []


def dfs(index):
    if index == 6:
        print(*lotto)
        return

    for i in range(len(test)):
        if index > 0 and lotto[index-1] > test[i]:
            continue

        if check_list[i] == 0:
            check_list[i] = 1
            lotto.append(test[i])
            dfs(index + 1)
            check_list[i] = 0
            lotto.pop()


while True:
    test = list(map(int, input().split()))
    if test[0] == 0:
        break
    check_list = [0] * test[0]
    del test[0]
    dfs(0)
    print()
