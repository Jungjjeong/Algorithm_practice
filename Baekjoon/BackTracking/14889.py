n = int(input())
s_arr = []

for i in range(n):
    s_arr.append(list(map(int, input().split(' '))))

team_arr = []
team = []
checked_list = [0] * n
min_result = 10000


def dfs(index):
    global team_arr
    global team

    if index == n and team_arr[0] == 1:
        team.append(team_arr[:])
        return

    for i in range(n):
        if 1 <= index < n/2 and team_arr[index-1] >= i+1:
            continue
        if index > n/2 and team_arr[index-1] >= i+1:
            continue

        if checked_list[i] == 0:
            checked_list[i] = 1
            team_arr.append(i+1)
            dfs(index + 1)
            checked_list[i] = 0
            team_arr.pop()


dfs(0)

for i in range(len(team)):
    t = team[i]
    print(t)
    sum_1 = 0
    for j in range(n//2):
        # 앞의 팀
        person = t[j]
        for k in t:
            sum_1 += s_arr[person-1][k-1]
    print(sum_1)

    sum_2 = 0
    for j in range(n//2):
        person = t[n//2+j]
        for k in t:
            sum_2 += s_arr[person-1][k-1]
    print(sum_2)

    print(sum_1 - sum_2)
    min_result = min(min_result, abs(sum_1 - sum_2))
    print(min_result)


print(team)
print(min_result)
