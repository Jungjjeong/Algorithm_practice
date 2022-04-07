from collections import deque


def solution(tickets):
    answer = []
    visit = [0] * len(tickets)

    tickets.sort(key=lambda x: x[1])

    def dfs(airport):
        if len(answer) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            if visit[i] == 0 and tickets[i][0] == airport:
                visit[i] = 1
                answer.append(tickets[i][1])
                if dfs(tickets[i][1]):
                    return True
                visit[i] = 0
                answer.pop()

    answer.append("ICN")
    dfs("ICN")

    return answer
