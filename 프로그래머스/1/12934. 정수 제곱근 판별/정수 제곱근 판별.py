def solution(n):
    answer = 0
    if n == 1:
        answer = 4
    for i in range(1,n):
        if n % i == 0:
            k = n // i
            if k == i:
                answer = (k+1)**2
                break;
            else:
                answer = -1
        else: 
            answer = -1
    return answer