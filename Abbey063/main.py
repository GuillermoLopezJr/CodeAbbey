from math import sqrt

def sieve(limit):
    nums = [True for i in range(limit)]

    primes = []
    for i in range(2, int(sqrt(limit))):
        if (nums[i] == True):
            for j in range(i*i, limit, i):
                nums[j] = False

    for i in range(2, limit):
        if(nums[i] == True):
            primes.append(i)

    return primes

def decompose(num, primes):
    prod = []
    while (num > 0):
        if (num == 1):
            break
        for p in primes:
            if (num % p == 0):
                prod.append(p)
                num = num // p
                break
            elif (p > num):
                break
    return prod

def printAns(ans):
    for nums in ans:
        for i in range(len(nums)):
            if (i != len(nums)-1):
                print(str(nums[i]) +"*", end ='')
            else: 
                print(str(nums[i]), end = ' ') 

def main():
    print("input data")
    TEST_CASES = int(input())

    primes = sieve(100000)

    ans = []
    for _ in range(TEST_CASES):
        num = int(input())
        prod = decompose(num, primes)
        ans.append(prod)
    
    print("\nanswer:")
    printAns(ans)

main()
