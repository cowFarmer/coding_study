def solution(s):
    s_list = list(map(int, s.split(" ")))
    answer = f"{min(s_list)} {max(s_list)}"
    return answer
    
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))