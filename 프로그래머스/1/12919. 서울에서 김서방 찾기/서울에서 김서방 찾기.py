def solution(seoul):
    answer = ''
    list_s = list(seoul)
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            a = str(i)
            break;
            
    answer = "김서방은 "+ a + "에 있다"
    return answer

