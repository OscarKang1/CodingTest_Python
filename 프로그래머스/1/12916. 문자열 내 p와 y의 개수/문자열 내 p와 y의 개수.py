def solution(s):
    answer = True
    
    list_s = list(s)
    a = list_s.count("p")+list_s.count("P")
    b = list_s.count("y") + list_s.count("Y")
    
    if a == b:
        answer= True
    else: 
        answer = False

    return answer