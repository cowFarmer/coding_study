def solution(n):
    answer = 0
    if n == 1:
        answer = 1
    
    if n**(1/2)%1 == 0:
        answer = (int(n**(1/2))+1)**2
    elif n**(1/2)%1 > 0:
        answer = -1
    return answer

print(solution(121))
print(solution(3))