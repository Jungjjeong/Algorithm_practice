lottery = [[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]


def solution(lottery):
    lot_dict = {}
    success = []
    answer = 0
    sum = 0

    for lot in lottery:
        if lot[0] in success:
                continue
        try:
            lot_dict[lot[0]] += 1
        except KeyError:
            lot_dict[lot[0]] = 1

        if lot[1] == 1:
            success.append(lot[0])
        
    if not success:
        return 0
    
    for i in success:
        sum += lot_dict[i]


    answer = int(sum/len(success))
    return answer


print(solution(lottery))
