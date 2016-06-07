def getPoints(n):
    pts = 1 + (n % 6)
    return pts

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        ran1, ran2 = map(int, input().split())
        dicePt1 = getPoints(ran1)
        dicePt2 = getPoints(ran2)
        ans.append(dicePt1 + dicePt2)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
