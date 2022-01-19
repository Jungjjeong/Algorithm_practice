n = int(input())
s_arr = []

for i in range(n):
    s_arr.append(list(map(int, input().split(' '))))

team_arr = []
team = []
checked_list = [0] * n
min_result = 0


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

# for t in team:
#     for i in team[0: n/2]:
#         print(i)

print(team)
