def genFibs(n):
    a = 0
    b = 1
    fibs = [0, 1]

    for i in range(n-2):
        nextVal = a + b 
        fibs.append(nextVal)
        a, b = b, nextVal

    return fibs
    
def find(x, xs):
    for i in range(len(xs)):
        if (x == xs[i]):
            return i

    return -1

def main():
    fibs = genFibs(1000) 

    print("input data")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        num = int(input())
        index = find(num, fibs)
        ans.append(index)
        
    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
