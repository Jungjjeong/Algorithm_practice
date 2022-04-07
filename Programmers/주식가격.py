def solution(prices):
    p_len = len(prices)
    answer = [0] * p_len

    for i in range(p_len):
        for j in range(i+1, p_len):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer
