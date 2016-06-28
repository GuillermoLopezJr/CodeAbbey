def checkDigit(n):
    return (n % 10 == 0)

def findDigit(num, index):
    if (index % 2 == 0):
        for digit in range(11):
            if (checkDigit(num+digit)):
                return digit
    else:
        for digit in range(11):
            expr = digit * 2
            if (expr >= 10):
                expr -= 9
            if (checkDigit(num+expr)):
                return digit

def isValidCreditCard(num):
    cardNum = [ch for ch in num]
    cardNum.reverse()

    result = 0
    for i in range(len(cardNum)):
        digit = int(cardNum[i])
        if (i % 2 == 0):
            result += digit
        else:
            result += digit*2
            if (digit*2 >= 10):
                result -= 9
    
    return checkDigit(result)

def swap(xs, index1, index2):
        temp = xs[index1]
        xs[index1] = xs[index2]
        xs[index2] = temp

def fixSwapError(cardNum):
        for i in range(len(cardNum)-1):
            swap(cardNum, i, i+1)
            if (isValidCreditCard(cardNum)):
                return (''.join(map(str,cardNum)))
            else:
                swap(cardNum, i, i+1)

def fixSingleError(cardNum, questIndex):
    cardNum.reverse()

    result = 0
    for i in range(len(cardNum)):
        if (i != questIndex):
            digit = int(cardNum[i])
            if (i % 2 == 0):
                result += digit
            else:
                result += digit*2
                if (digit*2 >= 10):
                    result -= 9

    digit = findDigit(result, questIndex)
    cardNum[questIndex] = digit
    cardNum.reverse()

    return (''.join(map(str,cardNum)))

def luhn(num):
    #since luhn algo works backwards
    questIndex = 15 - num.find('?')
    cardNum = [ch for ch in num]

    if (num.find('?') != -1):
        return fixSingleError(cardNum, questIndex)
    else:
        return fixSwapError(cardNum)

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        num = input()
        cardNum = luhn(num)
        ans.append(cardNum)
    
    print("\nanswer:")
    print(' '.join(map(str, ans)))
    
main()
