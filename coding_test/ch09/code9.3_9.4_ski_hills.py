MAX_DIFFERENCE = 17
MAX_HEIGHT = 100


def cost_for_range(heights, low, high):
    """
    heights는 모든 언덕의 높이를 가진 리스트입니다.
    low는 범위의 하한을 나타내는 정수입니다.
    high는 범위의 상한을 나타내는 정수입니다.

    언덕의 모든 높이를 low와 high 사이의 높이로 변경하는 비용을 반환합니다.
    """
    cost = 0
    for height in heights:
        if height < low:
            cost = cost + (low - height) ** 2
        elif height > high:
            cost = cost + (height - high) ** 2
    return cost


input_file = open('skidesign.in', 'r')
output_file = open('skidesign.out', 'w')

n = int(input_file.readline())

heights = []

for i in range(n):
    heights.append(int(input_file.readline()))

min_cost = cost_for_range(heights, 0, MAX_DIFFERENCE)

for low in range(1, MAX_HEIGHT + 1):
    result = cost_for_range(heights, low, low + MAX_DIFFERENCE)
    if result < min_cost:
        min_cost = result

output_file.write(str(min_cost) + '\n')

input_file.close()
output_file.close()
