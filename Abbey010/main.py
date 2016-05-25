def slope(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m

def yIntercept(x, y, m):
    b = y - m*x
    return b

def getPoint(x1, y1, x2, y2):
    m = round(slope(x1, y1, x2, y2))
    b = round(yIntercept(x1, y1, m))
    point = "(" + str(m) + ' ' + str(b) + ")"
    return point

def main():
    print("input data: ")
    TEST_CASES = int(input())
    
    ans = []
    for case in range(TEST_CASES):
        x1, y1, x2, y2 = map(int, input().split())
        ans.append(getPoint(x1, y1, x2, y2))

    print("\nanswer:")
    print(' '.join(ans))

main()
