def main():
    print("input data:")
    GUESSES = int(input())

    ones  = [x for x in range(10)]
    tens  = [x for x in range(10)]
    hunds = [x for x in range(10)]

    possibleNum = []
    for _ in range(GUESSES):
        num, corr = map(int, input().split())
        one = int(str(num)[2])
        ten = int(str(num)[1])
        hund = int(str(num)[0])

        if (corr == 0):
            ones[one] = -1 
            tens[ten] = -1
            hunds[hund] = -1
        elif (corr == 2):
            if (ones[one] == -1):
                possibleNum.append(tens[ten])
                possibleNum.append(hunds[hund])
            elif (tens[ten] == -1):
                possibleNum.append(ones[one])
                possibleNum.append(hunds[hun])
            elif (hunds[hund] == -1):
                possibleNum.append(ones[one])
                possibleNum.append(tens[ten])
            else:
                possibleNum.apend(ones[one])
                possibleNum.apend(tens[ten])
                possibleNum.apend(hunds[hund])

            







            


main()

        


