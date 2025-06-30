#TIC TAC TOE CODE
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    current_player = "X"
    moves = 0
    while moves < 9:
        print_board()
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
            if board[row][col] != " ":
                print("That spot is taken. Try again.")
                continue
        except:
            print("Invalid input. Try numbers 0, 1, or 2.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(current_player):
            print_board()
            print(f" Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board()
    print("It's a draw!")

play_game()
