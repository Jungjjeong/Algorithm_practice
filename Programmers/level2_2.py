from collections import deque
# deque는 양방향 데이터 삽입/삭제 가능

def solution(maps):
    # 이동할 네 가지 방향
    visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    n = len(maps) # 세로 길이
    m = len(maps[0]) # 가로 길이 

    Q = deque() # 큐 정의
    Q.append((0,0)) # 시작점 append
    visited[0][0] = 1


    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            # 미로 찾기 공간 벗어난 경우 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 0이면 무시
            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = 1
                Q.append((nx, ny))


    answer = maps[n-1][m-1]

    if answer == 1 :
        return -1
    return answer
