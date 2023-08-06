# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    stand_char = s[0]
    is_stand_char = ''
    is_not_stand_char = ''
    flag = False
    answer = 0
    
    for idx, c in enumerate(s):
        if flag:
            stand_char = s[idx]
        
        if stand_char == c:
            is_stand_char += c
        else:
            is_not_stand_char += c
        
        if len(is_stand_char) == len(is_not_stand_char):
            flag = True
            answer += 1
            is_stand_char = ''
            is_not_stand_char = ''
        else:
            flag = False
    if len(is_stand_char) > 0:
        answer += 1
    return answer

# print(solution("banana"))
# print(solution("abracadabra"))
print(solution("aaabbaccccabba"))