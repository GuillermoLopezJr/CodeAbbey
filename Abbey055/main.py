def dups(xs):
    dupList = []
    while (len(xs) != 0):
        x = xs.pop()
        if ( (x in xs) and (x not in dupList) ):
            dupList.append(x)

    return dupList
    
def order(xs):
    orderList = []
    while (len(xs) != 0):
        x = min(xs)
        xs.remove(x)
        orderList.append(x)
    
    return orderList
    
def main():
    print("input data: ")
    words = input().split()
    dupList = dups(words)
    ans = order(dupList) 
    
    print("\nanswer:")
    print(' '.join(ans))

main()
