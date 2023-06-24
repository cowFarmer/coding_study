# def solution(s):
#     nums = ["zero", "one", "two", "three", "four", "five", "six", \
#             "seven", "eight", "nine"]
#     answer = ""
    
#     tmp_num = ""
    
#     for i in s:
#         if i.isnumeric():
#             answer += i
#         else:
#             tmp_num += i
#             if len(tmp_num) >= 3:
#                 if tmp_num in nums:
#                     answer += str(nums.index(tmp_num))
#                     tmp_num = ""
#     answer = int(answer)
#     return answer

def solution(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", \
        "seven", "eight", "nine"]
    for i in range(len(nums)):
        s = s.replace(nums[i], str(i))
        print(s)
    return s

test1 = "one4seveneight"
test2 = "23four5six7"
test3 = "1zerotwozero3"

print(solution(test1))
print(solution(test2))
print(solution(test3))

# reference
# https://school.programmers.co.kr/learn/courses/30/lessons/81301