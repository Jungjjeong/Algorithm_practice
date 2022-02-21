from collections import deque


t = int(input())


def solution(y, x, dest_y, dest_x, chess):
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    q = deque()
    q.append((y, x))
    chess[y][x] = 0

    while q:
        y, x = q.popleft()

        if y == dest_y and x == dest_x:
            return chess[y][x]

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and chess[ny][nx] == 0:
                q.append((ny, nx))
                chess[ny][nx] = chess[y][x] + 1


for _ in range(t):
    n = int(input())

    chess = [[0 for _ in range(n)] for _ in range(n)]

    y, x = map(int, input().split(' '))
    dy, dx = map(int, input().split(' '))

    print(solution(y, x, dy, dx, chess))
