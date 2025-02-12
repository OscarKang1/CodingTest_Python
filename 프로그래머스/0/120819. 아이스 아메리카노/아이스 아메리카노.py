def solution(money):
    answer = []
    a = 0
    b = 0
    while money > 0 :
        money -= 5500
        a += 1
    
    if money < 0 :
        a = a-1
        b = money + 5500
    
    answer.append(a)
    answer.append(b)
    
    return answer