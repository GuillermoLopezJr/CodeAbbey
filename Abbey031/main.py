def shiftWord(word, shift):
    half1 = word[shift: ]
    half2 = word[0: shift]
    return (half1 + half2)

def main():
    print("input data:")
    TEST_CASES = int(input())
    
    ans = []
    for _ in range(TEST_CASES):
        shift, word = input().split()
        word = shiftWord(word, int(shift))
        ans.append(word)

    print("\nanswer:")
    print(' '.join(ans))

main()
