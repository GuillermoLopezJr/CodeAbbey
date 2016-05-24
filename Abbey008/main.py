def arithmeticSum(a_1, step, n):
   a_n = a_1 + (n-1)*step
   s_n = (a_1 + a_n)* n / 2
   return round(s_n)

def main():
    print("data: ")
    TEST_CASES = int(input())

    ans = []
    for case in range(TEST_CASES):
        a_1, step, n = map(int, input().split())
        ans.append(arithmeticSum(a_1, step, n))

    print("\nanswer:")
    print(' '.join(map(str,ans)))

main()
