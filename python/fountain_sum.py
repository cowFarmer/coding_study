def solution(numer1, denom1, numer2, denom2):
    answer = []
    if denom1 == denom2:
        answer = [numer1+numer2, denom1]
    elif denom1 % denom2 == 0:
        num = denom1 // denom2
        answer = [numer1+(numer2*num), denom1]
    elif denom2 % denom1 == 0:
        num = denom2 // denom1
        answer = [(numer1*num)+numer2, denom2]
    else:
        answer = [(numer1*denom2)+(numer2*denom1), denom1*denom2]
    
    divNum = 2
    while min(answer) >= divNum:
        if answer[0] % divNum == 0 and answer[1] % divNum == 0:
            answer[0] = answer[0] // divNum
            answer[1] = answer[1] // divNum
        else: divNum += 1
    return answer

print(solution(4,12,4,12))