def solution(arr):
    answer = []
    c = min(arr)
    if len(arr) == 1:
        answer.append(-1)
    
    else:
        for i in arr:
            if i != c:
                answer.append(i)
    
    
        


    return answer