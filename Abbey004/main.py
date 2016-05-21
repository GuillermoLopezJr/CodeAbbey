print("Enter number of test cases followed by data: ")
SIZE = int(input())

answers = []
for i in range(SIZE):
    a, b = map(int, input().split())
    answers.append(min(a,b))

print("answers: ")
for ans in answers:
    print(ans, end=" ")
