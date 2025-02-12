def solution(n, m):
    answer = []
    mini = []
    
    if n >= m :
        n , m = m, n
        
    for i in range(1,n+1):
        if n % i ==0 and m % i == 0:
            mini.append(i)
    
    answer.append(max(mini))
    
    mani = []
    for i in range(1,m+1):
        mani.append(i*n)
        
    for i in mani:
        if i % m == 0 :
            answer.append(i)
            break;
    return answer