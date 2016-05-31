def getDigits(num):
    digits = []

    while (num > 0):
        digit = num % 10
        num = num // 10
        digits.append(digit)
    
    digits.reverse()

    return digits

def bullsAndCows(code, guess):
    cDigits = getDigits(code) 
    gDigits = getDigits(guess)
    correct = 0
    semiCorrect = 0

    for i in range(len(cDigits)):
        if (cDigits[i] == gDigits[i]):
            correct += 1
        else:
            if (cDigits[i] in gDigits): 
                semiCorrect += 1
    
    return correct, semiCorrect

def main():
    print("input data:")
    code = int(input().split()[0]) 
    guesses = map(int, input().split())

    ans = []
    for guess in guesses:
        corr, semiCorr = bullsAndCows(code, guess)
        score = str(corr) + "-" + str(semiCorr)
        ans.append(score)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
