def solution(d, budget):
    d.sort()
    a = 0
   
    for i in range(len(d)):
        budget = budget - d[i]
        if budget >= 0:
            a = i + 1
        elif budget < 0:
            a = i
            break;
    return a