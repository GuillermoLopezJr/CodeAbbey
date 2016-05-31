def swap(nums, index):
    temp = nums[index+1]
    nums[index+1] = nums[index]
    nums[index] = temp

def bubbleSort(nums):
    swaps = 0
    passes = 0
    swapped = True

    while (swapped):
        swapped = False
        passes += 1
        for i in range(len(nums)-1):
            if (nums[i] > nums[i+1]):
                swap(nums,i)
                swaps += 1
                swapped = True
                 
    return passes, swaps

def main():
    print("input data: ")
    ignore = int(input())
    
    nums = [ int(x) for x in input().split() ]
    passes, swaps = bubbleSort(nums)

    print("\nanswer: ")
    print(passes, swaps)

main()  
