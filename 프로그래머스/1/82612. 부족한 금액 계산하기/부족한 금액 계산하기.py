def solution(price, money, count):
    answer = 0
    sum_price = 0
    
    for i in range(1,count+1):
        sum_price += i * price
        
    if money >= sum_price :
        answer = 0
    else:
        answer = sum_price - money
    return answer