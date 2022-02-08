from collections import deque as que

y = [1, 0, 0, -1]
x = [0, 1, -1, 0]  # 북동서남
stage = []

n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))  # 로봇 청소기 좌표와 방향

for i in range(n):
    stage.append(list(map(int, input().split(' '))))
# stage가 0이면 청소 가능한 빈칸, 1이면 벽, 2면 청소했음을 표시

stage[r][c] = 2  # 청소 했음
count = 1
q = que([(r, c)])  # que에 청소한 곳 좌표를 넣자


def solution(index):
