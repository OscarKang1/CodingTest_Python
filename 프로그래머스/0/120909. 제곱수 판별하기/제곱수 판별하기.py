def solution(n):
    answer = 0
    a = n**(1/2)
    
    if a % 1 == 0:
        answer = 1
    else:
        answer = 2
        
    return answer