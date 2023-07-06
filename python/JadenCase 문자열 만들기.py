def solution(s):
    answer = ""
    start = 0
    isfirstalpha = True
    
    for i in range(len(s)):
        if s[i] == " ":
            isfirstalpha = True
            answer += s[i]
        else:
            if isfirstalpha == True:
                answer += s[i].upper()
                isfirstalpha = False
            else:
                isfirstalpha = False
                answer += s[i].lower()
    return answer
print(solution("3people unFollowed me"))
print(solution("for the last week"))

print('3'.lower())