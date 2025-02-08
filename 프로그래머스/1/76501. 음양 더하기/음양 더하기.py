def solution(absolutes, signs):
    answer = 0
    
    for a,b in zip(absolutes, signs):
        if b == 1:
            answer += a
        else :
            answer -= a
            
    return answer