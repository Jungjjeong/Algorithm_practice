from itertools import combinations as com

n_len = int(input())
s_list = []
n_list = []
min_result = 10000000

for i in range(n_len):
    n_list.append(i)
    s_list.append(list(map(int, input().split(' '))))

team1_list = list(com(n_list, n_len//2))

for i in range(len(team1_list)):
    t1 = 0
    t2 = 0
    team2_set = set(n_list) - set(team1_list[i])

    team1 = list(com(team1_list[i], 2))
    team2 = list(com(team2_set, 2))

    for j in range(len(team1)):
        t1 += s_list[team1[j][0]][team1[j][1]] + \
            s_list[team1[j][1]][team1[j][0]]
        t2 += s_list[team2[j][0]][team2[j][1]] + \
            s_list[team2[j][1]][team2[j][0]]

    min_result = min(min_result, abs(t2 - t1))

print(min_result)
