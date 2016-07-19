def checkCond(n,a,b,c):
    isValid = True
    if (n != (a+b+c)):
        isValid = False
    if ((a**2 + b**2) != c**2):
        isValid = False

    return isValid

def pythagoreanTriple(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if (checkCond(n,a,b,c)):
                    return a,b,c


def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        num = int(input())
        a,b,c = pythagoreanTriple(num)
        ans.append(c**2)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
