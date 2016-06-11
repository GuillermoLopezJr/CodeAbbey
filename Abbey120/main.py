def selectionSort(xs):
    indices = []
    
    for i in range(len(xs)):
        maxIndex = 0
        size = len(xs)-i
        if (size == 1):
            break
        
        for j in range(size):
            if (xs[j] > xs[maxIndex]):
                maxIndex = j   

        temp = xs[size-1]
        xs[size-1] = xs[maxIndex]
        xs[maxIndex] = temp
        indices.append(maxIndex)

    return indices

def main():
    print("input data:")
    SIZE = int(input())

    xs = list(map(int, input().split()))
    ans = selectionSort(xs)

    print("\nanswer:")
    print(' '.join(map(str, ans)))
    
main()
