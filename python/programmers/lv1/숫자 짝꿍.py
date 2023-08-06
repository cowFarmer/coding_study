# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        count = min(X.count(str(i)), Y.count(str(i)))
        if count != 0:
            answer += str(i) * count
    
    if len(answer) < 1:
        return "-1"
    elif answer[0] == "0":
        return "0"
    else:
        return str(answer)
    
x = "1002"
y = "30005"

print(solution(x, y))