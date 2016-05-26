def approxSqrt(num, steps, r):
    if (steps == 0):
        return r
    else:
        d = num / r
        r = (r + d )/2
        return approxSqrt(num, steps-1, r) 

def main():
    print("input data: ")
    TEST_CASES = int(input())

    ans = []
    for case in range(TEST_CASES):
        num, steps = map(int, input().split())
        ans.append(approxSqrt(num, steps, 1))

    print("\nanswer: ")
    print(' '.join(map(str, ans)))

main()
