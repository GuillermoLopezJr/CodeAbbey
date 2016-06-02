def main():
    print("input data:")
    initNum = int(input())

    vals = []
    signs = []
    mod = 0
    modFound = False
    while not modFound:
        sign, val = input().split()
        signs.append(sign)
        vals.append(int(val))

        if (sign == '%'): 
            mod = int(val)
            modFound = True

    for i in range(len(vals)): 
        sign = signs[i]
        val = vals[i] 

        if (sign == "+"):
            initNum += val
            initNum %= mod
        elif (sign == "*"):
            initNum *= val
            initNum %= mod
        elif (sign == "%"):
            initNum %= mod

    print("\nanwer")
    print(initNum)


main()
