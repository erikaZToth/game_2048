import random
import os


def generate_board(board_size):
    board = [[" " for x in range(board_size)] for y in range(board_size)]
    return board


def print_board(board_size, board):
    print("2048")
    print("–" * 17)
    for x in range(board_size):
        print("| {} | {} | {} | {} |".format(
            board[x][0],
            board[x][1],
            board[x][2],
            board[x][3]
            ))
        print("–" * 17)
    return


def coordinate_is_available():
    pass


def random_numbers(board, board_size):
    available_numbers = [2, 2, 2, 2, 2, 2, 2, 4, 4, 4]
    random_numbers = random.choice(available_numbers)  
    available = False
    while available is False:
        random_x = random.randint(0, 3)
        random_y = random.randint(0, 3)
        if board[random_x][random_y] == " ":
            board[random_x][random_y] = random_numbers
            available = True
    return random_numbers


def jump_to_next_available_cell():
    pass


def moving_up(board, directions, board_size):
    for i in range(board_size):
        for j in range(board_size):
            # row_1_up(board, directions, board_size)
            if board[0][j] == " ":
                board[0][j] = board[1][j]
                board[1][j] = board[2][j]
                board[2][j] = board[3][j]
                board[3][j] = " "
            # row_2_up(board, directions, board_size)
            if board[1][j] == " ":
                board[1][j] = board[2][j]
                board[2][j] = board[3][j]
                board[3][j] = " "
            # row_3_up(board, directions, board_size)
            if board[2][j] == " ":
                board[2][j] = board[3][j]
                board[3][j] = " "
            if i > 0:
                if board[i][j] == board[i - 1][j] and board[i - 1][j] != " ": 
                    board[i - 1][j] *= 2  # bug: if row0 == row2 AND row3 == row4, then row3 won't be doubled!!!
                    board[i][j] = " "
                    if i < (board_size - 1):
                        board[i][j] = board[i + 1][j]
                        board[i + 1][j] = " "
                    else:
                        board[i][j] = " "
    # os.system("clear")
    end_of_game(board, directions, board_size)  
    return


def moving_down(board, directions, board_size):
    pass


def moving_left(board, directions, board_size):
    pass


def moving_right(board, directions, board_size):
    pass


def end_of_game(board, directions, board_size):      
    board_in_one_list = board[0] + board[1] + board[2] + board[3]
    board_in_one_list = [0 if i == " " else i for i in board_in_one_list]
    maximum_value = max(board_in_one_list)
    # player reached 2048?
    if maximum_value >= 2048:
        print_board(board_size, board)
        print("Congratulations! You've reached 2048!!! :)")  
        exit()
    # can we make any further steps?
    if 0 not in board_in_one_list:
        for i in range(board_size):
            for j in (1, board_size - 2):
                if board[i][j] == board[i][j - 1] or board[i][j] == board[i][j + 1]:
                    moving_on_board(board, directions, board_size)
        for i in range(1, board_size - 2):
            for j in (board_size):
                if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j]:
                    moving_on_board(board, directions, board_size)
                else:
                    print_board(board_size, board)
                    print("End of game")
                    exit()


def moving_on_board(board, directions, board_size):
    while True:
        direction = input("Enter direction: u (up), d (down), l (left), r (right): ")
        if direction == "u":
            moving_up(board, directions, board_size)                            
        elif direction == "d":
            end_of_game(board, directions, board_size)
        elif direction == "l":
            end_of_game(board, directions, board_size)
        elif direction == "r":
            end_of_game(board, directions, board_size)
        else:
            print("Please enter an available direction")
            continue
        random_numbers(board, board_size)
        print_board(board_size, board)
    # return


def main():
    board_size = 4
    board = generate_board(board_size)
    directions = ["u", "d", "l", "r"]  # u=up, d=down, l=left, r=right
    for i in range(2):
        random_numbers(board, board_size)
    print_board(board_size, board)
    moving_on_board(board, directions, board_size)
    # if end_of_game(board, directions, board_size) is True:
    #    exit()
    pass


if __name__ == "__main__":
    main()
