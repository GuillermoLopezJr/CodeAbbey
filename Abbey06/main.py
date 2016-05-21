print("Enter number of test Cases followed by data: ")

SIZE = int(input())
answers = []
for i in range(SIZE):
    a, b = map(int, input().split())
    answers.append(round(a/b))

print("\nanswer: ")
for ans in answers:
    print(ans, end=" ")
