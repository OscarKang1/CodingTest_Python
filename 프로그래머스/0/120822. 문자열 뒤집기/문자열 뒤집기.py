def solution(my_string):
    list_m = list(my_string)
    list_a = []
    for i in range(len(list_m)):
        
        list_a.insert(0,list_m[i])
        
    answer = ''.join(list_a)
    
    return answer