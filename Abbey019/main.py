def checkMatch(stack, openBracket):
    while (True):
        if (len(stack) == 0):
            return False

        x = stack.pop()
        if (x == openBracket):
            return True

def test(line):
    BRACKETS = "()[]{}<>"

    stack = []
    isMatch = True
    for ch in line:
        if (ch in BRACKETS):
            stack.append(ch)

        if (ch == ']'):
            isMatch = checkMatch(stack, '[')
        elif (ch == ')'):
            isMatch = checkMatch(stack, '(')
        elif (ch == '>'):
            isMatch = checkMatch(stack, '<')
        elif (ch == '}'):
            isMatch = checkMatch(stack, '{')
        
        if (isMatch == False):
            return 0

    isEmpty = [ b for b in BRACKETS if (b in stack) ] 
    if (len(isEmpty) == 0):
        return 1
    else:
        return 0


def main():
    print("input data")
    TEST_CASES = int(input())
    
    ans = []
    for _ in range(TEST_CASES):
        line = list(input())
        res = test(line)
        ans.append(str(res))

    print("\nanswer:")
    print(' '.join(ans))

main()
