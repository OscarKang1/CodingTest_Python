def solution(n, k):
    answer = 0
    s = 0
    if n >= 10:
        s = n // 10
        
    answer= 12000*n + 2000*(k-s)
    return answer