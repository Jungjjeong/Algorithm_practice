def solution(weights, head2head): 
    all_result_array = [] 
    answer = []


    for person_idx, match_result in enumerate(head2head):
        match_num, win_num, win_heavy = 0, 0, 0
        for idx, result in enumerate(match_result):
            if result != 'N':
                match_num += 1
            
            if result == 'W':
                win_num += 1
                if weights[person_idx] < weights[idx]:
                    win_heavy += 1

        
        try:
            all_result_array.append((win_num/ match_num, win_heavy, weights[person_idx], person_idx + 1))
        except ZeroDivisionError :
            all_result_array.append((0, win_heavy, weights[person_idx], person_idx + 1))
        
        
    all_result_array = sorted(all_result_array, key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    
    
    for i in all_result_array:
        answer.append(i[3])
    
    
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))