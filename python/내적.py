def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

a1 = [1,2,3,4]
b1 = [-3,-1,0,2]

print(solution(a1, b1))