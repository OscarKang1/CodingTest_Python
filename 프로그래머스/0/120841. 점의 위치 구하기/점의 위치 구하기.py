def solution(dot):
    answer = 0
    a = dot[0]
    b = dot[1]
    
    if a > 0 and b > 0:
        answer = 1
    if a < 0 and b > 0:
        answer = 2
    if a < 0 and b < 0:
        answer = 3
    if a > 0 and b < 0:
        answer = 4
    return answer