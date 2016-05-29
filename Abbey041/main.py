def findMedian(nums):
    nums.sort()
    return nums[1]
    
def main():
    print("data: ")
    TEST_CASES = int(input())

    ans = []
    for case in range(TEST_CASES):
        nums = list(map(int, input().split()))
        mid = findMedian(nums)
        ans.append(mid)

    print("\nanswer: ")
    print( ' '.join(map(str, ans)))

main()
