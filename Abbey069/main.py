def fibs(n):
    a = 0
    b = 1
    
    fibList = [0,1]
    for i in range(n-2):
        nextTerm = a + b
        fibList.append(nextTerm)
        a, b = b, nextTerm

    return fibList

def numDivisibleBy(num, fibList):
    for i in range(3, len(fibList)):
        if (fibList[i] % num == 0):
            return i

    return -1

def main():
    print("input data:")
    TEST_CASES = int(input())

    fibList = fibs(10000)
    nums = [ int(x) for x in input().split() ]
    
    ans = []
    for num in nums:
        d = numDivisibleBy(num, fibList) 
        ans.append(str(d))

    print("\nanswer:")
    print(' '.join(ans))

main()
