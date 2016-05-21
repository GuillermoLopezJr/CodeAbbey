print("input data: ")
SIZE = int(input())

numLists = []
for i in range(SIZE):
   nums = map(int, input().split())
   numLists.append(nums)

print("answer: ")
for xs in numLists:
    print(sum(xs), end=" ")
