def solution(my_string, n):
    answer = ''
    list_m = list(my_string)
    for i in range(len(my_string)):
        answer += ''.join(list_m[i]*n)
    return answer