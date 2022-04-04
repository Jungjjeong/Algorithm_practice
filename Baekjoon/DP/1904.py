n = int(input())

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2

# 점화식 f(x) = f(x-2) + f(x-1)

for i in range(1, n-1):
    dp[i+2] = (dp[i] + dp[i+1]) % 15746

print(dp[n] % 15746)
