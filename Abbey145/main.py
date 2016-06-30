def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []

    for _ in range(TEST_CASES):
        A, B, M = map(int, input().split())
        res = 1
        for _ in range(B):
            res = (res * A) % M
        ans.append(res)

    print("\nanswer:")
    print(' '.join(map(str,ans)))
            
main()
