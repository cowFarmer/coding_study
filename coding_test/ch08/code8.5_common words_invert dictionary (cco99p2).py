def invert_dictionary(d):
    """
    d는 문자열을 숫자로 매핑하는 딕셔너리입니다.

    d의 반전된 딕셔너리를 반환합니다.
    """
    inverted = {}
    for key in d:
        num = d[key]
        if not num in inverted:
            inverted[num] = [key]
        else:
            inverted[num].append(key)
    return inverted
