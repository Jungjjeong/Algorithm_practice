s_num = int(input())
s_list = list(map(int, input().split(' ')))
student_num = int(input())


def change(num):
    if s_list[num] == 0:
        s_list[num] = 1
    elif s_list[num] == 1:
        s_list[num] = 0


for i in range(student_num):
    s, num = map(int, input().split(' '))
    if s == 1:
        change(num-1)

        for n in range(2, s_num + 1):
            r = num*n-1
            if r < s_num:
                change(r)
            else:
                break

    elif s == 2:
        change(num-1)

        for n in range(1, s_num // 2 + 1):
            r_minus = num-1-n
            r_plus = num-1+n

            if r_minus < 0 or r_minus >= s_num or r_plus < 0 or r_plus >= s_num:
                break

            if s_list[r_minus] == s_list[r_plus]:
                change(r_minus)
                change(r_plus)
            else:
                break

for i in range(0, s_num, 20):
    print(*s_list[i:i+20])


# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다.
# -> 시뮬레이션은 문제를 정말 자세하고,, 잘 읽어야 한다.
