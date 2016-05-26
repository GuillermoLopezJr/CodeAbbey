def avg(nums):
    avg = sum(nums) / len(nums)    
    return round(avg)

def main():
    print("input data:")
    TEST_CASES = int(input())
    
    ans = []
    for case in range(TEST_CASES):
        nums = list(map(int, input().split()))
        nums.pop()
        ans.append(avg(nums))
    
    print("\nanswer: ")
    print(' '.join(map(str, ans)))

main()
