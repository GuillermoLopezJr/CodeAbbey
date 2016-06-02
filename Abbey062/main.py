def sieve(limit):
    nums = [True for i in range(limit+1)]

    primes = []
    for i in range(2, limit+1):
        if (nums[i] == True):
            primes.append(i)
            for j in range(i*i, limit+1, i):
                nums[j] = False

    return primes

def primesInRange(lb, ub, primeList):
    xs = primeList[ primeList.index(lb) : primeList.index(ub)+1 ]
    return (len(xs))
    
def main():
    print("input data: ")
    TEST_CASES = int(input())
    
    primeList = sieve(3000000)
    ans = []
    for _ in range(TEST_CASES):
        lb, ub = map(int, input().split())
        amount = primesInRange(lb, ub, primeList)
        ans.append(amount)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
