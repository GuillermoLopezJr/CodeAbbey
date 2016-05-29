def isPalindrome(xs):
    if (xs == list(reversed(xs))):
        return "Y"
    else:
        return "N"
    
def main():
    print("input data:")
    TEST_CASES = int(input())

    punc = ".,!?-; "
    ans = []
    for _ in range(TEST_CASES):
        xs = [x.lower() for x in input() if x not in punc]
        ans.append(isPalindrome(xs))

    print("\nanswer: ")
    print(' '.join(ans))
        
main()
