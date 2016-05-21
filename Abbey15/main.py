print("input data:")
nums = []
nums = list(map(int, input().split()))

minNum = nums[0]
maxNum = nums[0]

for num in nums:
    if (num < minNum):
        minNum = num
    elif (num > maxNum):
        maxNum = num

print("answer\n{0} {1}".format(maxNum, minNum))
