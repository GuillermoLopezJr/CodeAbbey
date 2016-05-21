def toCelsius(tempF):
    cel = (tempF - 32) / 1.8
    return round(cel)

print("data: ")
data = list(map(int, input().split()))
SIZE = data[0]

ans = []
for i in range(1,SIZE+1):
    cel = toCelsius(data[i])
    ans.append(cel)

print("\nanswer: ")
print(' '.join(map(str, ans)))
