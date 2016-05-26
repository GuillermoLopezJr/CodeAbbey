def getDigitSum(num):
    digitSum = 0
    while(num != 0):
        digit = num % 10
        digitSum += digit
        num = num // 10
    
    return digitSum

def main():
    print("input data: ")
    TEST_CASES = int(input())

    ans = []
    for case in range(TEST_CASES):
        a, b, c = map(int, input().split())
        num = a * b + c
        ans.append(getDigitSum(num))
    
    print("\nanswer: ")
    print(' '.join(map(str, ans)))

main()
