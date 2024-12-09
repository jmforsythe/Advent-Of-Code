nums = [int(i) for i in open("input.txt").read().strip()]
id = 0
ptr = 0
data = [-1 for i in range(sum(nums))]
for i in range(0, len(nums)-1, 2):
    for j in range(nums[i]):
        data[ptr] = id
        ptr += 1
    id += 1
    ptr += nums[i+1]
if len(nums)%2:
    for j in range(nums[-1]):
        data[ptr] = id
        ptr += 1
data2 = [i for i in data]

leftPtr = 0
rightPtr = len(data)-1
while leftPtr < rightPtr:
    while leftPtr < len(data) and data[leftPtr] != -1:
        leftPtr += 1
    while rightPtr >= 0 and data[rightPtr] == -1:
        rightPtr -= 1
    if leftPtr >= rightPtr:
        break
    data[leftPtr] = data[rightPtr]
    data[rightPtr] = -1

print(sum(i*p for i, p in enumerate(data) if p != -1))

rightPtr = len(data)-1
leftPtr = 0
while leftPtr < rightPtr:
    while leftPtr < len(data2) and data2[leftPtr] != -1:
        leftPtr += 1
    while data2[rightPtr] == -1 or (rightPtr > 0 and data2[rightPtr] == data2[rightPtr-1]):
        rightPtr -= 1
    size = 0
    while rightPtr+size < len(data2) and data2[rightPtr] == data2[rightPtr+size]:
        size += 1
    if all(data2[leftPtr+i] == -1 for i in range(size)):
        for i in range(size):
            data2[leftPtr+i] = data2[rightPtr+i]
            data2[rightPtr+i] = -1
        leftPtr += size
    else:
        tempLeftPtr = leftPtr
        while tempLeftPtr < rightPtr and not all(data2[tempLeftPtr+i] == -1 for i in range(size)):
            tempLeftPtr += 1
        if tempLeftPtr < rightPtr:
            for i in range(size):
                data2[tempLeftPtr+i] = data2[rightPtr+i]
                data2[rightPtr+i] = -1
    rightPtr -= 1
print(sum(i*p for i, p in enumerate(data2) if p != -1))
