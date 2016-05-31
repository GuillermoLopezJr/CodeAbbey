from math import sqrt

def triType(a,b,c):
    tri = ""
    hyp = sqrt( pow(a,2) + pow(b,2) )
    
    if (c == hyp):
        tri = "R"
    elif (c < hyp):
        tri = "A"
    else:
        tri = "O"

    return tri

def main():
    print("input data: ")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        a,b,c = map(int, input().split())
        ans.append(triType(a,b,c))
    
    print("\nanswer: ")
    print(' '.join(ans))

main()
