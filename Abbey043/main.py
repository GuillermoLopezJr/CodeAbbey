TEST_CASES = int(input())

ans = []
for case in range(TEST_CASES):
    num = float(input())
    pts = int(6*num + 1)
    ans.append(pts)

print("\nanswer:")
print(' '.join(map(str, ans)))
