grid = [ [1, 8, 3, 2], [7, 4, 6, 5] ]

def solution(grid):
    dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    # dp = [[0] * len(grid)] * len(grid[0])

    for h_idx, h in enumerate(grid):
        for w_idx, w in enumerate(grid[0]):
            if h_idx == 0 and w_idx == 0:
                dp[0][0] = grid[0][0]
                continue
            elif w_idx == 0:
                dp[h_idx][w_idx] = dp[h_idx-1][w_idx] + grid[h_idx][w_idx]
                continue 
            elif h_idx == 0:
                dp[h_idx][w_idx] = dp[h_idx][w_idx-1] + grid[h_idx][w_idx]
                continue
            dp[h_idx][w_idx] = min(dp[h_idx-1][w_idx], dp[h_idx][w_idx-1]) + grid[h_idx][w_idx]
        

    min_path_sum = dp[len(grid)-1][len(grid[0])-1]
    return min_path_sum

print(solution(grid))