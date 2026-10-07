import random


board = [str(i) for i in range(1, 10)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(symbol):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    return any(all(board[pos] == symbol for pos in line) for line in win_positions)

def is_tie():
    return all(space in ['X','O'] for space in board)

def user_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid number. Choose between 1 and 9.")
                continue
            if board[move-1] in ['X','O']:
                print("That spot is already taken.")
                continue
            board[move-1] = 'O'
            break
        except ValueError:
            print("Please enter a valid integer.")

def computer_move():
    free_positions = [i for i in range(9) if board[i] not in ['X','O']]
    if free_positions:
        move = random.choice(free_positions)
        board[move] = 'X'
        print(f"Computer chose position {move+1}")


print("Welcome to Tic-Tac-Toe!")
board[4] = 'X'  
print_board()

while True:
    user_move()
    print_board()
    if check_winner('O'):
        print("You win!")
        break
    if is_tie():
        print("It's a tie!")
        break

    computer_move()
    print_board()
    if check_winner('X'):
        print("Computer wins!")
        break
    if is_tie():
        print("It's a tie!")
        break
