import math

def sieve(limit):
    nums = [True for i in range(limit)]

    primes = []
    for i in range(2, int(math.sqrt(limit))):
        if (nums[i] == True):
            for j in range(i*i, limit, i):
                nums[j] = False

    for i in range(2, limit):
        if(nums[i] == True):
            primes.append(i)

    return primes

def main():
    print("input data:")
    TEST_CASES = int(input())

    indices = list(map(int, input().split()))
    primeList = sieve(10000000)
    ans = []

    for index in indices:
        prime = primeList[index-1]
        ans.append(prime)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
