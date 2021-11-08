"""
Name: <Queen Hamilton, II>
<lab10>.py
"""


def board_build():
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return position_list


def display_board(position_list):
    print("-" * 14)
    counter = 0
    for i in range(3):
        print("|", end=" ")
        for x in range(3):
            print(position_list[counter], end=" | ")
            counter += 1
        print("\n")
    print("-" * 14)


def place_spot(position_list, spot, marker):
    position_list[spot] = marker


def legal_move(position_list, spot):
    if position_list[spot] == "X" or position_list[spot] == "O" or (9 < spot < 1):
        return False
    else:
        return True


def game_won(position_list):
    win_con = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in win_con:
        counter = 0
        for spot in condition:
            if position_list[spot - 1] == "X":
                counter += 1
            if counter == 3:
                return "X wins!!"
        counter = 0
        for spot in condition:
            if position_list[spot - 1] == "O":
                counter += 1
            if counter == 3:
                return "O wins!!"


def game_over(position_list, turn_count):
    if game_won(position_list) == "X wins!!" or game_won(position_list) == "O wins!!" or turn_count == 9:
        return True
    else:
        return False


def play_game():
    board = board_build()
    display_board(board)
    turn_count = 0
    end_game = game_over(board, turn_count)
    while not end_game:
        if turn_count % 2 == 0:
            marker = "X"
            spot = int(input("X's turn - Choose a number: ")) - 1
            if legal_move(board, spot):
                place_spot(board, spot, marker)
                turn_count += 1
        else:
            marker = "O"
            spot = int(input("O's turn - Choose a number: ")) - 1
            if legal_move(board, spot):
                place_spot(board, spot, marker)
                turn_count += 1
        display_board(board)
        end_game = game_over(board, turn_count)
    if game_won(board):
        print(game_won(board))
    else:
        print("Tie game!")


def main():
    # add other function calls here
    play_game()


main()
