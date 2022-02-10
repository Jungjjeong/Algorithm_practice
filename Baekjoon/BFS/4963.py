from collections import deque

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]
map_list = []


def solution(rx, ry):
    global map_list
    q = deque()
    q.append((rx, ry))
    map_list[ry][rx] = 0

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(map_list[0]) or ny < 0 or ny >= len(map_list) or map_list[ny][nx] == 0:
                continue
            elif map_list[ny][nx] == 1:
                q.append((nx, ny))
                map_list[ny][nx] = 0


while True:
    w, h = map(int, input().split(' '))
    if w == 0 and h == 0:
        break

    map_list = []
    count = 0

    for _ in range(h):
        map_list.append(list(map(int, input().split(' '))))

    for i in range(h):
        for j in range(w):
            if map_list[i][j] == 1:
                solution(j, i)
                count += 1

    print(count)
