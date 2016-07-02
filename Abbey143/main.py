def GCD(x,y):
    remFlag = False

    while (remFlag == False):
        print(x,y)
        if (x > y):
            rem = x % y
            x = rem
            if (rem == 0):
                remFlag = True
        else:
            rem = y % x
            y = rem
            if (rem == 0):
                remFlag = True
    return (x if (x > y) else y)

def main():
    print("input data:")
    TEST_CASES = int(input())

    for _ in range(TEST_CASES):
        x, y = map(int, input().split())
        d = GCD(x,y)
        print(d)

main()
