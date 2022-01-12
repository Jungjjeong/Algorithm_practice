arr = [4,5,2,3,1]
k = 2

def solution(arr, k):
    answer = 0
    min_num = min(arr)

    for i in range(len(arr)-1,0,-1):
        for j in range(len(arr)):
            if abs(j - i) <= k and arr[i] < arr[j] and i > j:
                print(arr)
                arr[i], arr[j] = arr[j], arr[i]
                answer += 1
                  
    print(arr)
    return answer

print(solution(arr,k))