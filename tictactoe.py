def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"
    winner = None
    moves = 0

    while not winner and moves < 9:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player
            moves += 1
            winner = check_winner(board)
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


play_game()
