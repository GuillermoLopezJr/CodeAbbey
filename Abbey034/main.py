from math import sqrt, exp

def solve(a,b,c,d,lb,ub):
    mid = (ub - lb)/2
    x = lb + mid
    
    res = a*x + b*sqrt(x**3) - c*exp(-x/50) - d

    if (abs(res) < .0000001):
        return x
    else:
        if (res > 0):
            ub = x
        else:
            lb = x

        return solve(a,b,c,d,lb,ub)

def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for case in range(TEST_CASES):
        a,b,c,d = [float(x) for x in input().split()]
        ans.append(solve(a,b,c,d,0,100))
        

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
