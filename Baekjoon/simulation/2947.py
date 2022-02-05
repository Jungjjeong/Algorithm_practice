from tempfile import tempdir


n_list = list(map(int, input().split(' ')))

while True:
    isTrue = False

    for i in range(4):
        if n_list[i] > n_list[i+1]:
            temp = n_list[i]
            n_list[i] = n_list[i+1]
            n_list[i+1] = temp
            print(*n_list)

    for i in range(4):
        if n_list[i] < n_list[i+1]:
            isTrue = True
        else:
            isTrue = False
            break

    if isTrue == True:
        break
