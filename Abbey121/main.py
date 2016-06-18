def insertionSort(xs):
    shifts = []
    for i in range(1, len(xs)):
        shift = 0
        for j in range(i):
            if (xs[i] < xs[j]):
                temp = xs[i]
                xs[i] = xs[j]
                xs[j] = temp
                shift += 1
        shifts.append(shift)

    return shifts
    
def main():
    print("input data")
    SIZE = int(input())
    nums = [int(x) for x in input().split()]

    ans = insertionSort(nums)
    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
