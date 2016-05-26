def wsd(num):
    digits = []
    while(num != 0):
        digit = num % 10
        digits.append(digit)
        num = num // 10
    digits.reverse() 

    wsd = 0
    for i in range(len(digits)):
        wsd += (i+1) * digits[i]
    return wsd

def main():
    print("input data: ")
    TEST_CASES = int(input())
    nums = list(map(int, input().split()))
    
    print("\nanswer: ")
    for num in nums:
        print(wsd(num), end=' ')
    
main()
