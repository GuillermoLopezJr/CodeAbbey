def main():
    print("data input:")
    span = int(input().split()[1])

    indices = [0 for _ in range(span)]
    data = list(map(int, input().split()))
        
    for i in data:
        indices[i-1] += 1

    print("\nanswer:")
    print(' '.join(map(str, indices)))

main()
