def CollatzSequence(num):
    count = 0 
    while (num != 1):
        count += 1
        if (num % 2 == 0):
            num /= 2
        else:
            num = 3*num + 1

    return count

def main():
    print("input data: ")
    TEST_CASES = int(input())

    nums = list(map(int, input().split()))
    ans = []

    for num in nums:
        ans.append(CollatzSequence(num))

    print("\nanswer: ")
    print(' '.join(map(str, ans)))

main()
