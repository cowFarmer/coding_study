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
