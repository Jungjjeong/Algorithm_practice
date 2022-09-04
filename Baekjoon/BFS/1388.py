n, m = map(int, input().split(' '))
graph = []
count = 0

for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    pre = '@'
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != pre:
                count += 1
        pre = graph[i][j]

for j in range(m):
    pre = '@'
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != pre:
                count += 1
        pre = graph[i][j]


print(count)
