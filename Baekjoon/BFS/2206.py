from collections import deque


n, m = map(int, input().split(' '))
map_list = []

for _ in range(n):
    map_list.append(list(map(int, input())))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# 3차원 배열 (벽을 부순거와 안부수고 이동한 걸 나눠서 저장)


def solution(ry, rx, break_wall):
    global map_list
    global visited

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    q = deque()
    q.append((ry, rx, break_wall))
    map_list[ry][rx] = 1
    visited[ry][rx][break_wall] = 1

    while q:
        y, x, b = q.popleft()

        if y == n-1 and x == m-1:
            return visited[y][x][b]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if map_list[ny][nx] == 0 and visited[ny][nx][b] == 0:
                    q.append((ny, nx, b))
                    visited[ny][nx][b] = visited[y][x][b] + 1
                elif map_list[ny][nx] == 1 and b == 0:
                    q.append((ny, nx, 1))
                    visited[ny][nx][1] = visited[y][x][b] + 1

    return -1


print(solution(0, 0, 0))
