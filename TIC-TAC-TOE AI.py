def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board, player):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_states

def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best = -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best = max(score, best)
        return best
    else:
        best = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best = min(score, best)
        return best

def ai_move(board):
    best_score = -1
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = 'O'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe: You (X) vs AI (O)")

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell taken, try again.")
            continue

        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break

        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

        ai_move(board)
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
