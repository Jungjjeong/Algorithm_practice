import sys
input = sys.stdin.readline

n = int(input())
r_num = int(input())
r_list = list(map(int, input().split()))
photo_dict = {}
answer = []

for i in range(r_num):
    if r_list[i] in photo_dict.keys():
        photo_dict[r_list[i]][0] += 1
    else:
        if len(photo_dict) < n:
            photo_dict[r_list[i]] = [1, i]
        else:
            del_photo_dict = sorted(
                photo_dict.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_photo_dict[0][0]
            photo_dict.pop(del_key)
            photo_dict[r_list[i]] = [1, i]

for k in photo_dict.keys():
    answer.append(k)

answer.sort()
print(*answer)
