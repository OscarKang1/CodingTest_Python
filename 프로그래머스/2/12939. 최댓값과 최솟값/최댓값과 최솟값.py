def solution(s):
    answer = ''
    a = s.split(" ")
    
    for i in range(len(a)):
        a[i] = int(a[i])
        
    
    a.sort()
    



    return str(a[0])+" "+str(a[-1])