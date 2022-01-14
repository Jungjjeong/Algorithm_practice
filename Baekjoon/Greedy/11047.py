n, k = map(int, input().split(' '))
v_arr = []

for _ in range(n):
    v_arr.append(int(input()))

i = n - 1
count = 0

while k > 0:
    if i == -1:
        break

    count += k // v_arr[i]
    k %= v_arr[i]
    i -= 1

print(count)
