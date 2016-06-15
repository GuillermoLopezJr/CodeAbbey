def getMeet(d, v1, v2):
    x = d / (v1+v2) 
    m = x * v1  
    return m

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        dist, v1, v2 = map(int, input().split())
        m = getMeet(dist, v1, v2)
        ans.append(m)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
