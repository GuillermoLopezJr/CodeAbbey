def fillList(data):
    f = open("db-ip.txt", 'r')

    for line in f:
        xs = line.split() 
        start = int(xs[0], 36)
        end = start + int(xs[1], 36)
        country = xs[2]
        info = [start, end, country] 
        data.append(info)

def binarySearch(ip, xs):
    lb = 0
    ub = len(xs)

    found = False
    while (not found):
        mid = (ub - lb) // 2
        k = lb + mid

        start_k = xs[k][0]
        end_k = xs[k][1]
        start_k_1 = xs[k+1][0]

        if ( (start_k <= ip) and (start_k_1 > ip) ):
            found = True
        else:
            if (start_k > ip):
                ub = k
            else:
                lb = k

    return xs[k][2] 

def main():
    data = [] 
    fillList(data)
    
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        ip = int(input(), 36)
        country = binarySearch(ip, data)
        ans.append(country)

    print("\nanswer:")
    print(' '.join(ans))

main()
