n = int(input())
meeting_t = []

for _ in range(n):
    s, e = map(int, input().split(' '))
    meeting_t.append([s, e])

meeting_t.sort(key=lambda x: (x[1], x[0]))

count = 1
end_t = meeting_t[0][1]

for i in range(1, n):
    if meeting_t[i][0] >= end_t:
        count += 1
        end_t = meeting_t[i][1]
    else:
        pass

print(count)
