def isTri(a,b,c):
    flag = 1
    if (a + b < c):
        flag = 0 
    elif (a + c < b):
        flag = 0
    elif (b + c < a):
        flag = 0
    return flag

def main():
    print("data: ")
    TEST_CASES = int(input())

    ans = []
    for case in range(TEST_CASES):
        a,b,c = map(int, input().split())
        ans.append(isTri(a,b,c))

    print("\nanswer:")
    print(' '.join(map(str,ans)))

main()
