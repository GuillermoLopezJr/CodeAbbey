def linearCongruentGen(A, C, M, x0):
    xNext = (A*x0 + C) % M
    return xNext

def getWord(lenWord, x0):
    CONSONANT = "bcdfghjklmnprstvwxz"
    VOWELS    = "aeiou"
    A, C, M   = 445, 700001, 2097152

    word = ""
    for i in range(1,lenWord+1):
        x0 = linearCongruentGen(A,C,M,x0) 

        if (i % 2 == 0):
            index = x0 % len(VOWELS)
            word += VOWELS[index]
        else:
            index = x0 % len(CONSONANT) 
            word += CONSONANT[index]

    return word, x0

def main():
    print("input data:")
    amountOfWords, seed = map(int, input().split()) 
    lenWords = list(map(int, input().split()))

    ans = []
    for i in range(amountOfWords):
        word, seed = getWord(lenWords[i], seed) 
        ans.append(word)

    print("\nanswer:")
    print(' '.join(ans)) 

main()
