def main():
    print("input data:")
    numVals = int(input())

    vals = [ float(x) for x in input().split() ]

    ans = []
    for i in range(len(vals)):
        if (i == 0):
            ans.append(vals[i])
        elif (i == len(vals)-1):
            ans.append(vals[i])
        else:
            val = (vals[i-1] + vals[i] + vals[i+1])/3
            ans.append(val)

    print("\nanswer:")
    print(' '.join(map(str, ans)))

main()
