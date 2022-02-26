import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split(' ')))
operator_list = list(map(int, input().split(' ')))

max = float('-inf')
min = float('inf')
answer = n_list[0]

def dfs(index):
    global answer
    global max, min

    if index == n-1:
        if answer > max:
            max = answer
        if answer < min:
            min = answer
        return

    for i in range(4):
        if operator_list[i] > 0:
            operator_list[i] -= 1
            temp = answer
            if i == 0:
                answer += n_list[index + 1]
            elif i == 1:
                answer -= n_list[index + 1]
            elif i == 2:
                answer *= n_list[index + 1]
            elif i == 3:
                if answer < 0:
                    answer = -(-answer // n_list[index + 1])
                else:
                    answer //= n_list[index + 1]
            dfs(index + 1)
            operator_list[i] += 1
            answer = temp

dfs(0)

print(max)
print(min)