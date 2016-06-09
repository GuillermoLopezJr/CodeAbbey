def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)

def getCombinations(n, k):
    c = fact(n) / ( fact(k) * fact(n-k) )
    return round(c)
    

def main():
    print("input data:")
    TEST_CASES = int(input())
    
    ans = []
    for _ in range(TEST_CASES):
        n, k = map(int, input().split())
        c = getCombinations(n, k)
        ans.append(c)
    
    print("\nanswer")
    print(' '.join(map(str, ans)))

main()
