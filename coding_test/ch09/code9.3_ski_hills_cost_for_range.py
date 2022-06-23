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
