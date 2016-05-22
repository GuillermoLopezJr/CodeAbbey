def loopCount(x):
    count = 0
    terms = []
    while(x not in terms):
        terms.append(x)
        count += 1
        x *= x
        digits = len(str(x))
        amount = 8 - digits
        xStr = '0'*amount + str(x)  
        x = xStr[2:-2]
        x = int(x)

    return count

def main():
    print("input data:")
    TEST_CASES = int(input())
    initVals = list(map(int, input().split()))

    ans = []
    for val in initVals:
       ans.append(loopCount(val)) 

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
