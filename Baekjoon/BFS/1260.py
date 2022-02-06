from collections import deque as que

n, m, v = map(int, input().split(' '))

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1


visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)  # 매번 -1헤주기 싫다.


def dfs(root):
    visited_dfs[root] = 1
    print(root, end=' ')
    for i in range(1, n + 1):
        if visited_dfs[i] == 0 and graph[root][i] == 1:
            dfs(i)


def bfs(root):
    q = que()
    q.append(root)
    visited_bfs[root] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, n + 1):
            if visited_bfs[i] == 0 and graph[node][i] == 1:
                q.append(i)
                visited_bfs[i] = 1


dfs(v)
print()
bfs(v)
