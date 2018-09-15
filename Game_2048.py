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


def board_in_one_list():
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


def moving_up(board, directions, board_size):
    for i in range(board_size):
        for j in range(board_size):
            # moving numbers up:
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
            # doubles values (numbers) if they are equal, and moves the following numbers up: 
            if i > 0:
                if board[i][j] == board[i - 1][j] and board[i - 1][j] != " ": 
                    board[i - 1][j] *= 2  # doubles numbers if they are equal. Bug: if row0 == row2 AND row3 == row4, then row3 won't be doubled!!!
                    board[i][j] = " "
                    if i < (board_size - 1):
                        board[i][j] = board[i + 1][j]  # moves the following numbers up
                        board[i + 1][j] = " "
                    else:
                        board[i][j] = " "  # empty last row
    # os.system("clear")
    end_of_game(board, directions, board_size)  
    return


def moving_down(board, directions, board_size):
    for i in range(board_size - 1, -1, -1):
        for j in range(board_size):
            # row_4_down(board, directions, board_size)
            if board[3][j] == " ":
                board[3][j] = board[2][j]
                board[2][j] = board[1][j]
                board[1][j] = board[0][j]
                board[0][j] = " "
            # row_3_down(board, directions, board_size)
            if board[2][j] == " ":
                board[2][j] = board[1][j]
                board[1][j] = board[0][j]
                board[0][j] = " "
            # row_2_down(board, directions, board_size)
            if board[1][j] == " ":
                board[1][j] = board[0][j]
                board[0][j] = " "
            elif i < 3:
                if board[i][j] == board[i + 1][j] and board[i + 1][j] != " ": 
                    board[i + 1][j] *= 2  # bug: if row0 == row2 AND row3 == row4, then row3 won't be doubled!!!
                    board[i][j] = " "
                    if i > 0:
                        board[i][j] = board[i - 1][j]
                        board[i - 1][j] = " "
                    else:
                        board[i][j] = " "
    # os.system("clear")
    end_of_game(board, directions, board_size)  
    return


def moving_left(board, directions, board_size):
    for i in range(board_size):
        for j in range(board_size):
            # column_2_left(board, directions, board_size)
            if board[i][0] == " ":
                board[i][0] = board[i][1]
                board[i][1] = board[i][2]
                board[i][2] = board[i][3]
                board[i][3] = " "
            # column_3_left(board, directions, board_size)
            if board[i][1] == " ":
                board[i][1] = board[i][2]
                board[i][2] = board[i][3]
                board[i][3] = " "
            # column_4_left(board, directions, board_size)
            if board[i][2] == " ":
                board[i][2] = board[i][3]
                board[i][3] = " "
            if j > 0:
                if board[i][j] == board[i][j - 1] and board[i][j - 1] != " ": 
                    board[i][j - 1] *= 2  # bug: if column0 == column2 AND column3 == column4, then column3 won't be doubled!!!
                    board[i][j] = " "
                    if j < (board_size - 1):
                        board[i][j] = board[i][j + 1]
                        board[i][j + 1] = " "
                    else:
                        board[i][j] = " "
    # os.system("clear")
    end_of_game(board, directions, board_size)  
    return


def moving_right(board, directions, board_size):
    for i in range(board_size):
        for j in range(board_size, -1, -1):
            # column_3_right(board, directions, board_size)
            if board[i][3] == " ":
                board[i][3] = board[i][2]
                board[i][2] = board[i][1]
                board[i][1] = board[i][0]
                board[i][0] = " "
            # column_2_right(board, directions, board_size)
            if board[i][2] == " ":
                board[i][2] = board[i][1]
                board[i][1] = board[i][0]
                board[i][0] = " "
            # column_1_right(board, directions, board_size)
            if board[i][1] == " ":
                board[i][1] = board[i][0]
                board[i][0] = " "
            if j < 3:
                if board[i][j] == board[i][j + 1] and board[i][j + 1] != " ":
                    board[i][j + 1] *= 2
                    board[i][j] = " "
                    if j > 0:
                        board[i][j] = board[i][j - 1]
                        board[i][j - 1] = " "
                    else:
                        board[i][j] = " "
    # os.system("clear")
    end_of_game(board, directions, board_size)  
    return


def end_of_game(board, directions, board_size):      
    board_in_one_list = board[0] + board[1] + board[2] + board[3]
    board_in_one_list = [0 if i == " " else i for i in board_in_one_list]
    maximum_value = max(board_in_one_list)
    # player reached 2048?
    if maximum_value >= 2048:
        print_board(board_size, board)
        print("CONGRATULATIONS! YOU'VE REACHED 2048!!! :)")  
        exit()
    # can we make any further steps?
    if 0 not in board_in_one_list:
        for i in range(board_size):
            for j in (1, board_size - 2):
                if board[i][j] == board[i][j - 1] or board[i][j] == board[i][j + 1]:
                    moving_on_board(board, directions, board_size)
        for i in range(1, board_size - 2):
            for j in range(board_size):  # TypeError: 'int' object is not iterable -> ???
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
            moving_down(board, directions, board_size)
        elif direction == "l":
            moving_left(board, directions, board_size)
        elif direction == "r":
            moving_right(board, directions, board_size)
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
