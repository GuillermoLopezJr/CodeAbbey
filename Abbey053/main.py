def canEat(rowK, colK, rowQ, colQ):
    yes = 'Y'
    no  = 'N'

    if (rowK == rowQ or colK == colQ):
        return yes

    row = 7
    col = 7

    #goes down left
    c = colQ
    r = rowQ
    while(c != 0 and r != row):
        c -= 1
        r += 1
        if (r == rowK) and (c == colK):
            return yes
    
    #goes down right
    c = colQ
    r = rowQ
    while(c != col and r != row):
        c += 1
        r += 1
        if (r == rowK) and (c == colK):
            return yes

    #goes up right
    c = colQ
    r = rowQ
    while (c != col and r != 0):
        c += 1
        r -= 1
        if (r == rowK) and (c == colK):
            return yes

    #goes up left
    c = colQ
    r = rowQ
    while (c != 0 and r != 0):
        c -= 1
        r -= 1
        if (r == rowK) and (c == colK):
            return yes

    return no

def main():
    print("input data:")
    TEST_CASES = int(input())

    row = 8
    col = 8

    alpha = "abcdefgh"
    ans = []
    for _ in range(TEST_CASES):
        king, queen = input().split()

        colK = alpha.index(king[0])
        rowK = row - int(king[1])
        colQ = alpha.index(queen[0]) 
        rowQ = row - int(queen[1])

        a = canEat(rowK, colK, rowQ, colQ) 
        ans.append(a)
        
    print("\nanswer:")
    print(' '.join(ans))

main()
