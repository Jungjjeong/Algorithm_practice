from collections import deque


n = int(input())

graph = [[] for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    i_list = list(map(int, input().split()))

    for j in range(n):
        if i_list[j] == 1:
            graph[i].append(j)


def solution(i, num):
    visit = [0] * (n+1)
    q = deque()
    q.append(num)

    while q:
        number = q.popleft()
        for g in graph[number]:
            if visit[g] == 0:
                visit[g] = 1
                answer[i][g] = 1
                q.append(g)


for i in range(n):
    solution(i, i)
    print(*answer[i])
