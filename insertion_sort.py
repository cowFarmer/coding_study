import random

def findInsertIdx(ary, data):
    findIdx = -1
    for i in range(0, len(ary)):
        if (ary[i] < data): # >, <가 오름차순, 내림차순 결정
            findIdx = i
            break
    if findIdx == -1:
        return len(ary)
    else:
        return findIdx

before = []
after = []

for i in range(10):
    before.append(random.randint(0,200))
# before = [random.randint(0,200) for _ in range(10)]

print("정렬 전 -->", before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print("정렬 후 -->", after)