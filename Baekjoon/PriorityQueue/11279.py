import heapq
import sys

input = sys.stdin.readline
n = int(input())

max_heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    elif num >= 0:
        heapq.heappush(max_heap, (-num, num))
