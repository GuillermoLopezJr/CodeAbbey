def squareList(nums):
    listSquared = list(map(lambda x: x*x, nums))
    return sum(listSquared)

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
       nums = [int(x) for x in input().split()]
       ans.append(squareList(nums))

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
