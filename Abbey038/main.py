from math import sqrt

def descriminant(a,b,c):
    d = pow(b,2) - 4*a*c
    return d

def roots(a,b,c):
    d = descriminant(a,b,c) 
    
    left = -b / (2*a)
    right = sqrt(abs(d)) / (2*a)

    if (d >= 0):
       x1 = round(left + right) 
       x2 = round(left - right)
       
       if (x1 > x2):
           return str(x1) + " " + str(x2)
       else:
           return str(x2) + " " + str(x1)

    else:
       left = round(left)
       right = round(right)
       x1 = str(left) + "+" + str(right) + "i"
       x2 = str(left) + "-" + str(right) + "i"
       return x1 + " " + x2
    
def main():
    print("input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        a, b, c = map(int, input().split())
        ans.append(roots(a,b,c))

    print("\nanswer:")
    for i in range(len(ans)):
        if (i != len(ans)-1):
            print(ans[i] + "; ", end='')
        else:
            print(ans[i])
            
main()
