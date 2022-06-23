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


input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

n = int(input_file.readline())

intervals = []

for i in range(n):
    interval = input_file.readline().split()
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    intervals.append(interval)

max_covered = 0

for fired in range(n):
    result = num_covered(intervals, fired)
    if result > max_covered:
        max_covered = result

output_file.write(str(max_covered) + '\n')

input_file.close()
output_file.close()
