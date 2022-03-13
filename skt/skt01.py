def solution(money, costs):
	answer = 0
	money_unit = [[1], [5], [10], [50], [100], [500]]
	coin = len(costs)
	dp = [0 for _ in range(money + 1)]
	dp[0] = 1
	
	for i in range(coin):
		money_unit[i].append(costs[i])

	# 화폐 단위, 생산 단가로 2차원 배열 생성
	print(money_unit)

	
	print(money)

	for m in money_unit:
		for i in range(m[0], money + 1):
			if i - m[0] >= 0:
				dp[i] += dp[i-m[0]]

	return answer



print(solution(4578, [1, 4, 99, 35, 50, 1000]))