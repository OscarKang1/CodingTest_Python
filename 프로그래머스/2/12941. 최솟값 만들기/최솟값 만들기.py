def solution(A,B):
    
    A.sort(reverse = True)
    B.sort()
    c = 0
    for i,j in zip (A,B):
        c += i*j
    

    return c