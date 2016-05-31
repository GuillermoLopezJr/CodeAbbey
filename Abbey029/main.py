def swap(xs, index):
    temp = xs[index+1]
    xs[index+1] = xs[index]
    xs[index] = temp

def bubbleSort(nums,indices):
    swapped = True
    while (swapped):
        swapped = False
        for i in range(len(nums)-1):
            if (nums[i] > nums[i+1]):
                swap(nums,i)
                swap(indices, i) 
                swapped = True

def main():
    print("input data: ")
    SIZE = int(input())
    
    nums = [ int(x) for x in input().split() ]
    indices = [ x for x in range(1, SIZE+1) ]
    bubbleSort(nums, indices)

    print("\nanswer: ")
    print(' '.join(map(str, indices)))

main()  
