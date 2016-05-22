def beats(p1, p2):
    tie   = 0
    p1Win = 1
    p2Win = 2
    if(p1 == p2):
        return tie
    elif (p1 == 'R'):
        if (p2 == 'S'):
            return p1Win
        else:
            return p2Win
    elif (p1 == 'P'):
        if (p2 == 'R'):
            return p1Win
        else:
            return p2Win
    elif (p1 == 'S'):
        if (p2 == 'P'):
            return p1Win
        else:
            return p2Win

def getWinner(games):
    p1Score = 0
    p2Score = 0
    for game in games:
        p1 = game[0]
        p2 = game[1]
        outcome = beats(p1, p2)
        if (outcome == 1):
            p1Score += 1
        elif (outcome == 2):
            p2Score += 1

    winner = -1
    if (p1Score > p2Score):
       winner = 1 
    elif (p2Score > p1Score):
        winner = 2 
    else:
        winner = 0
    return winner
        
def main():
    print("input data: ")
    TEST_CASES = int(input())
    
    ans = []
    for i in range(TEST_CASES):
        case = input().split()
        ans.append(getWinner(case))
    
    print("\nanswer: ")
    print(' '.join(map(str, ans)))

main()
