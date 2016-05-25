def getBMI(w, h):
    BMI = w / (h*h)
    return BMI

def getGrade(BMI):
    NORMAL_WEIGHT = 18.5
    OVER_WEIGHT = 25.0
    OBESE = 30.0

    if (BMI < NORMAL_WEIGHT):
        return "under"
    elif (BMI < OVER_WEIGHT):
        return "normal"
    elif (BMI < OBESE):
        return "over"
    else:
        return "obese"

def main():
    print("input data:")
    TEST_CASES = int(input())
    
    ans = []
    for case in range(TEST_CASES):
        weight, height = map(float, input().split())
        BMI = getBMI(weight, height)
        grade = getGrade(BMI)
        ans.append(grade)

    print("\nanswer: ")
    print(' '.join(ans))

main()
