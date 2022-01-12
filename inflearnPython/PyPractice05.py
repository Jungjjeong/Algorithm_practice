graph = {100: set([67, 66]),
         67: set([100, 82, 63]),
         66: set([100, 73, 69]),
         82: set([67, 61, 79]),
         63: set([67]),
         73: set([66]),
         69: set([66, 65, 81]),
         61: set([82]),
         79: set([82, 87, 77]),
         65: set([69, 84, 99]),
         81: set([69]),
         87: set([79, 31, 78]),
         77: set([79]),
         84: set([65]),
         99: set([65]),
         31: set([87]),
         78: set([87])}

# 깊이우선탐색 : 정점에서 한 방향으로 내려감 , 막힌 정점은 포기하고 따라온 간선으로 되돌아가기
# stack 사용 (FILO)
def 깊이우선탐색min(graph, start):
    방문 = []
    stack = [start]
    while stack:
        n = stack.pop(0)
        if n not in 방문:
            방문.append(n)
            차집합 = graph[n] - set(방문) # 이미 방문한 친구들은 stack에 넣어줄 필요가 없어용
            if len(차집합) == 0:
                방문 += stack
                break
            stack.append(min(차집합))
            print(f'visited : {방문}')
            print(f'stack : {stack}')
    return 방문

def 깊이우선탐색max(graph, start):
    방문 = []
    stack = [start]
    while stack:
        n = stack.pop(0)
        if n not in 방문:
            방문.append(n)
            차집합 = graph[n] - set(방문) # 이미 방문한 친구들은 stack에 넣어줄 필요가 없어용
            if len(차집합) == 0:
                방문 += stack
                break
            stack.append(max(차집합))
            print(f'visited : {방문}')
            print(f'stack : {stack}')
    return 방문

print(''.join([chr(i) for i in 깊이우선탐색min(graph, 100)]))
print(''.join([chr(i) for i in 깊이우선탐색max(graph, 100)]))

# 너비우선탐색 : 가까운 정점 먼저 방문, 먼 정점은 나중에 방문
# queue 사용 (FIFO)