# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    # 길이
    height_length = len(park)
    width_length = len(park[0])
    
    # 방향
    directions = ['E', 'W', 'S', 'N']
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]
    
    # 시작 지점 찾기
    for row in range(height_length):
        if 'S' in park[row]:
            cur = [row, park[row].index('S')]
            break
    
    # 이동
    for route in routes:
        direct, count = route.split(' ')
        count = int(count)
        is_success = True
        
        # 미리 이동해볼 tmp
        tmp = [cur[0], cur[1]]
        move = directions.index(direct)
        
        # count 만큼 direct 방향으로 move
        for _ in range(count):
            print(tmp)
            tmp = [tmp[0]+dh[move], tmp[1]+dw[move]]
            
            # out of park or 'X'
            if tmp[0] >= height_length or tmp[1] >= width_length or tmp[0] < 0 or tmp[1] < 0 or park[tmp[0]][tmp[1]] == 'X':
                is_success = False
                break

        # tmp가 조건에 부합하면 cur 이동
        if is_success:
            cur = tmp
            
    return cur

# park = ["OSO","OOO","OXO","OOO"]
# routes = ["E 2","S 3","W 1"]

park = ["OOOOO", "OOOOO", "OOSOO", "OOOOO", "OOOOO"]
routes = ["E 2", "E 1", "W 4", "W 1", "S 2", "S 1", "N 4", "N 1"]

print(solution(park, routes))