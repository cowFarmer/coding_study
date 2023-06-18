# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    for idx, i in enumerate(photo):
        for j in i:
            if j in name:
                answer[idx] += yearning[name.index(j)]
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

solution(name, yearning, photo)