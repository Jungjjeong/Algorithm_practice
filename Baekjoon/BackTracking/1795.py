l, c = map(int, input().split(' '))
c_arr = list(map(str, input().split(' ')))
c_arr.sort()

password = []
check_list = [0] * c
vowel_set = {'a', 'e', 'i', 'o', 'u'}
consonant_set = set(list(x for x in c_arr if x not in vowel_set))


def dfs(index):
    if index == l:
        if len(set(password) & vowel_set) >= 1 and len(set(password) & consonant_set) >= 2:
            print(*password, sep='')

    for i in range(c):
        if index > 0 and c_arr.index(password[index - 1]) > c_arr.index(c_arr[i]):
            continue

        if check_list[i] == 0:
            check_list[i] = 1
            password.append(c_arr[i])
            dfs(index + 1)
            check_list[i] = 0
            password.pop()


dfs(0)
