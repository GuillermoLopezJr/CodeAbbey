def isWinner(board, player):
    #for horizontal
    if (board[0][0] == player and board[0][1] == player and board[0][2] == player):
        return True
    elif (board[1][0] == player and board[1][1] == player and board[1][2] == player):
        return True
    elif (board[2][0] == player and board[2][1] == player and board[2][2] == player):
        return True

    #for vertical
    elif (board[0][0] == player and board[1][0] == player and board[2][0] == player):
        return True
    elif (board[0][1] == player and board[1][1] == player and board[2][1] == player):
        return True
    elif (board[0][2] == player and board[1][2] == player and board[2][2] == player):
        return True

    #for diagonal
    elif (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    elif (board[2][0] == player and board[1][1] == player and board[0][2] == player):
        return True
    else: 
        return False
    
def getPosition(move):
    row = int(move // 3)
    col = move % 3
    return row, col

def getWinningMove(moves):
    ROW = 3
    COL = 3
    playerX = 'X'
    playerO = 'O'
    board = [ [' ' for c in range(COL)] for r in range(ROW) ]
    
    player = playerX
    moveCounter = 0
    for move in moves:
        moveCounter += 1
        row, col = getPosition(move-1)
        board[row][col] = player

        if (isWinner(board, player)):
            return moveCounter

        player = playerO if player == playerX else playerX

    return 0

def main():
    print("Input data:")
    TEST_CASES = int(input())

    ans = []
    for _ in range(TEST_CASES):
        moves = list(map(int, input().split()))
        m = getWinningMove(moves)
        ans.append(m)
    
    print("\nanswer")
    print(' '.join(map(str, ans)))

main()        
