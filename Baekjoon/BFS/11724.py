n, m = map(int, input().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split(' '))
    graph[i][j] = graph[j][i] = 1

visited = [0] * (n+1)
count = 0


def solution(num):
    global count

    for i in range(1, n+1):
        if graph[num][i] == 1 and visited[i] == 0:
            visited[i] = 1
            solution(i)


for i in range(1, n+1):
    if visited[i] == 0:
        visited[i] = 1
        solution(i)
        count += 1

print(count)
