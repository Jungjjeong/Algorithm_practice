def solution(price, money, count):
    sum = 0
    
    for i in range(1, count + 1):
        sum += price * i
    
    if money < sum : return sum - money
    elif money >= sum: return 0


print(solution(3, 20, 4))