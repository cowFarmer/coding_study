# ccc18j1, Telemarketers

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# Telemarketer 번호: 첫 번째 자리는 8 또는 9, 네 번째 자리는 8 또는 9,
# 두 번째 자리와 세 번째 자리의 수는 같음.
if ((num1 == 8 or num1 == 9) and
        (num4 == 8 or num4 == 9) and
        (num2 == num3)):
    print('ignore')
else:
    print('answer')
