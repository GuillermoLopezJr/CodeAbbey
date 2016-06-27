def findDigit(num, index):
    if (index % 2 == 0):
        for i in range(10):
            if ((num+i) % 10 == 0):
                return i


def luhn(num):
    cardNum = [ch for ch in num]
    cardNum.reverse()

    res = 0
    
    questionMarkFound = False
    index = -1

    for i in range(len(cardNum)):
        if (cardNum[i] == '?'):
            questionMarkFound = True
            index = 15 - i
        else:
            digit = int(cardNum[i])
            if (i % 2 == 0):
                res += digit
            else:
                res += digit *2
                if (digit*2 >= 10):
                    res -= 9

    if (questionMarkFound):
        digit = findDigit(res, index)

    if (res % 10 == 0):
        print("valid")
    else:
        print("invalid")




def main():
    print("input data:")
    TEST_CASES = int(input())

    for _ in range(TEST_CASES):
        num = input()
        luhn(num)
    
            


main()
