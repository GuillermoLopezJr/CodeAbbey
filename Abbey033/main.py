def strBinary(n):
    b = bin(n)[2:]
    zeroes = '0' * (8-len(b))
    b = zeroes + b
    return b

def binToInt(b):
    return int(b[1:],2)

def distance(b):
    count = 0
    for ch in b:
        if (ch == '1'):
            count += 1

    return count

def main():
    print("input data:")

    ans = []
    for code in map(int, input().split()):
        b = strBinary(code)

        if (distance(b) % 2 == 0):
            n = binToInt(b)
            ch = chr(n)
            ans.append(ch)

    print("\nanswer:")
    print(''.join(ans))

main()
