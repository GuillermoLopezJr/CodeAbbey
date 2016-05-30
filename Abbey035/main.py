def getYrs(balance, reqSum, rate):
    rate = rate / 100
    
    yrs = 0
    while (balance < reqSum):
        balance += balance*rate
        yrs += 1

    return yrs

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        initAmount, reqSum, rate = map(int, input().split())
        yrs = getYrs(initAmount, reqSum, rate)
        ans.append(yrs)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
