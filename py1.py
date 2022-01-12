def solution(rows, columns, swipes):
    answer = []
    arr = [[0 for i in range(columns)] for j in range(rows)]
    count = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = count
            count += 1
    
    temp = 0

    for s in swipes:
        y = s[1] - 1
        x = s[2] - 1

        print(arr[y][x])

        if s[0] == 1 or s[0] == 3:

            while(True):
                if y == s[3] - 1 and x != s[4] - 1:
                    y = s[1] - 1
                    x += 1
                elif y != s[3] - 1 and x == s[4] - 1:
                    x = s[2] - 1
                    y += 1
                elif y == s[3] - 1 and x == s[4] - 1:
                    break
                print(y,x)
                arr[y][x] = arr[y + dy[s[0] - 1]][x + dx[s[0] - 1]]
                print(arr)
                y = y + dy[s[0] - 1]
                x = x + dx[s[0] - 1]
            print(arr)
solution(4, 3, [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]])