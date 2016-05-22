def countVowels(sentence):
    vowelCount = 0
    for word in sentence:
        for ch in word:
            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'y'):
                vowelCount += 1
    return vowelCount

def main():
    print("input data: ")
    TEST_CASES = int(input())

    sentences = []
    for case in range(TEST_CASES):
        sentences.append(input().split())

    ans = []
    for sentence in sentences:
        ans.append(countVowels(sentence))

    print("\nanswer: ")
    print(' '.join(map(str,ans)))

main()
