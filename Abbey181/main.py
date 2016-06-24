from math import sqrt

def main():
    print("input data:")
    expression = input().split()

    stack = []
    binaryOps = ["mul", "div", "sub", "add", "mod"]
    uniaryOps = ["sqrt"]
    for token in expression:
        res = -1
        if (token in binaryOps):
            b = stack.pop()
            a = stack.pop()
            if (token == "mul"):
                res = a * b
            elif (token == "div"):
                res = a / b
            elif (token == "add"):
                res = a + b
            elif (token == "sub"):
                res = a - b
            elif (token == "mod"):
                res = a % b
        elif (token in uniaryOps):
            a = stack.pop()
            if (token == "sqrt"):
                res = sqrt(a)
        else:
            res = int(token)

        stack.append(res)

    res = stack.pop()
    print("\nanswer:")
    print(round(res))
    
main()
