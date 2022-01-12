def solution(scores):
    answer = ''
    
    for wid in range(len(scores[0])):
        arr = []
        
        for i in range(len(scores)):
            arr.append(scores[i][wid])
            
        if (min(arr) == scores[wid][wid] and arr.count(min(arr)) == 1) or (max(arr) == scores[wid][wid] and arr.count(max(arr)) == 1):
            arr.pop(wid)

        avg = sum(arr) / len(arr)

        if avg >= 90:
            answer = answer + 'A'
        elif 80 <= avg < 90:
            answer = answer + 'B'
        elif 70 <= avg < 80:
            answer = answer + 'C'
        elif 50 <= avg < 70:
            answer = answer + 'D'
        else:
            answer = answer + 'F'
        
    return answer

print(solution(	[[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))