def solution(n):
    answer = 0
    a = str(n)
    b = str()
    list_n = list(a)
    list_n.sort(reverse = True)
    for i in list_n:
        b += i
    
    answer = int(b)
    return answer