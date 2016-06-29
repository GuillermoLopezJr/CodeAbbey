def partition(xs, left, right):
    lt = left
    rt = right
    direction = "left"  #which side has empty space
    pivot = xs[left]
    
    while (lt < rt):
        if (direction == "left"):
            if (xs[rt] > pivot):
                rt = rt - 1
            else:
                xs[lt] = xs[rt]
                lt += 1
                direction = "right"
        else:
            if (xs[lt] < pivot):
                lt += 1
            else:
                xs[rt] = xs[lt]
                rt -= 1
                dir = "left"

    #lt = rt ==> both points to empty cell were pivot should return
    xs[lt] = pivot
    return lt


#return list of left-right ranges for each call of recursive function 

def quickSort(xs, left, right,ans):
    a = str(left) +"-" + str(right)
    ans.append(a)

    pivotPos = partition(xs, left, right)
    if ((pivotPos-left) > 1):
        quickSort(xs, left, pivotPos-1,ans)
    if ((right-pivotPos) > 1):
        quickSort(xs, pivotPos+1, right,ans)

def main():
    print("input data:")
    SIZE = int(input())
    nums = [int(x) for x in input().split()]
    
    ans = []
    quickSort(nums, 0, SIZE-1,ans)
    print("\nanswer")
    print(' '.join(ans))

main()
