def solution(s):
    answer = True
    list_s = list(s)
    if len(list_s) == 4:
        answer = True
    elif len(list_s) == 6 :
        answer = True
    else:
        answer = False
        
    for i in list_s:
        if i.isalpha():
            answer = False
        
            
    return answer