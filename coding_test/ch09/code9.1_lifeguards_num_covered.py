def num_covered(intervals, fired):
    """
    intervals는 인명구조원들의 근무 간격 리스트입니다.
    각 간격은 [시작, 종료] 리스트입니다.
    fired는 해고하는 인명구조원의 인덱스입니다.

    해고된 인명구조원을 제외한 모든 인명구조원의 근무 시간 단위 수를 반환합니다.
    """
    covered = set()
    for i in range(len(intervals)):
        if i != fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):
                covered.add(j)
    return len(covered)

