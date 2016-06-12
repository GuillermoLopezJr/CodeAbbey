def getxNext(A, C, M, x0):
    xNext = (A*x0 + C) % M
    return xNext

def getNthStep(A, C, M, x0, N):
    for i in range(N):
        xNext = getxNext(A, C, M, x0)
        x0 = xNext

    return x0

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        A, C, M, x0, N = map(int, input().split())
        n = getNthStep(A, C, M, x0, N)
        ans.append(n)
    
    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
