from collections import deque


def solution(n, computers):
    visit = [0] * n
    answer = 0

    def bfs(num):
        q = deque()
        q.append(num)
        visit[num] = 1

        while q:
            num = q.popleft()

            for i in range(n):
                if visit[i] == 0 and computers[num][i] == 1:
                    q.append(i)
                    visit[i] = 1

    for i in range(n):
        if visit[i] == 0:
            bfs(i)
            answer += 1

    return answer
