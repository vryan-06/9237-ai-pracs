import math

def evaluate_board(board):
    if check_win(board, "X"):
        score = 1
    elif check_win(board, "O"):
        score = -1
    else:
        score = 0

    return score

def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    return True

def game_over(board):
    return check_win(board, "X") or check_win(board, "O") or check_tie(board)

def print_board(board):
    for i in range(3):
        print("-------------")
        row = "| "
        for j in range(3):
            row += board[i][j] + " | "
        print(row)
    print("-------------")


def get_player_move(board):
    valid_move = False
    while not valid_move:
        move = input("Enter your move (row, column): ")
        row, col = move.split(",")
        row = int(row) - 1
        col = int(col) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Try again.")
        elif board[row][col] != "":
            print("That space is already taken. Try again.")
        else:
            valid_move = True

    return row, col

def get_computer_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

print_board(board)

while not game_over(board):
    row, col = get_player_move(board)
    board[row][col] = "O"
    print_board(board)
    if game_over(board):
        break
    print("Computer's turn:")
    row, col = get_computer_move(board)
    board[row][col] = "X"
    print_board(board)

if check_win(board, "X"):
    print("Computer wins!")
elif check_win(board, "O"):
    print("Player wins!")
else:
    print("Tie game.")
