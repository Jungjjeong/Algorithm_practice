n = int(input())

inequality_list = list(map(str, input().split(' ')))

num_list = []
check_list = [0] * 10

min_num = 9999999999
min_str = ''
max_num = 0
max_str = ''


def dfs(index):
    global min_num, max_num
    global min_str, max_str

    if index == n+1:
        num = int("".join(map(str, num_list)))
        if min_num > num:
            min_num = num
            min_str = ''.join(map(str, num_list))
        if max_num < num:
            max_num = num
            max_str = ''.join(map(str, num_list))
        return

    for i in range(10):
        if index == 0:
            num_list.append(i)
            check_list[i] = 1
            dfs(index + 1)
            check_list[i] = 0
            num_list.pop()
        elif check_list[i] == 0:
            if inequality_list[index - 1] == '>' and num_list[index - 1] > i or inequality_list[index - 1] == '<' and num_list[index - 1] < i:
                num_list.append(i)
                check_list[i] = 1
                dfs(index+1)
                check_list[i] = 0
                num_list.pop()


dfs(0)
print(max_str)
print(min_str)
