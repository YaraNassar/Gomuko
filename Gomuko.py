
def is_empty(board):
    '''This function returns True iff there are no stones on the board board.'''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    ''''This function analyses the sequence of length length that ends at location (y end, x end). The function returns "OPEN" if the sequence is open, 
    "SEMIOPEN" if the sequence if semi-open, and "CLOSED" if the sequence is closed.'''


    if d_y == 0 and d_x == 1:
        left_side = True
        right_side = True

        x_end2 = x_end - length + 1
        if x_end2 == 0:
            left_side = False
        if x_end == len(board[0]) - 1:
            right_side = False
        if x_end != len(board[0]) - 1:
            if board[y_end][x_end + 1] != " ":
                right_side = False
        if x_end2 != 0:
            if board[y_end][x_end2 - 1] != " ":
                left_side = False

        if left_side == False and right_side == False:
            return "CLOSED"
        if left_side == True and right_side == True:
            return "OPEN"
        else:
            return "SEMI-OPEN"

    if d_y == 1 and d_x == 0:
        top = True
        bottom = True

        y_end2 = y_end - length + 1

        if y_end2 == 0:
            top = False
        if y_end == len(board) - 1:
            bottom = False

        if y_end2 != 0:
            if board[y_end2 - 1][x_end] != " ":
                top = False
        if y_end != len(board) - 1:
            if board[y_end + 1][x_end] != " ":
                bottom = False


        if top == False and bottom == False:
            return "CLOSED"
        if top == True and bottom == True:
            return "OPEN"
        else:
            return "SEMI-OPEN"

    if d_y == 1 and d_x == 1:
        top_left = True
        bottom_right = True

        y_end2 = y_end - length + 1
        x_end2 = x_end - length + 1

        if y_end2 == 0 or x_end2 == 0:
            top_left = False
        if y_end == len(board) - 1 or x_end == len(board[0]) - 1:
            bottom_right = False

        if y_end2 != 0 and x_end2 != 0:
            if board[y_end2 - 1][x_end2 - 1] != " ":
                top_left = False
        if y_end != len(board) - 1 and x_end != len(board[0]) - 1:
            if board[y_end + 1][x_end + 1] != " ":
                bottom_right = False

        if top_left == False and bottom_right == False:
            return "CLOSED"
        if top_left == True and bottom_right == True:
            return "OPEN"
        else:
            return "SEMI-OPEN"

    if d_y == 1 and d_x == -1:
        top_right = True
        bottom_left = True

        y_end2 = y_end - length + 1
        x_end2 = x_end + length - 1

        if y_end2 == 0 or x_end2 == len(board[0]) - 1:
            top_right = False
        if y_end == len(board) - 1 or x_end == 0:
            bottom_left = False

        if y_end2 != 0 and x_end2 != len(board[0]) - 1:
            if board[y_end2 - 1][x_end2 + 1] != " ":
                top_right = False
        if y_end != len(board) - 1 and x_end != 0:
            if board[y_end + 1][x_end - 1] != " ":
                bottom_left = False


        if top_right == False and bottom_left == False:
            return "CLOSED"
        if top_right == True and bottom_left == True:
            return "OPEN"
        else:
            return "SEMI-OPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    ''''This function analyses the row of squares that starts at the location (y start,x start)
and goes in the direction (d y,d x). The function returns a tuple whose first element is the number of open
sequences of colour col of length length in the row R, and whose second element is the number of
semi-open sequences of colour col of length length in the row R.''' 
    open_seq_count = 0
    semi_open_seq_count = 0

    if d_y == 0 and d_x == 1:
        y_end = y_start
        for i in range(length - 1, len(board[0])):
            x_end = i
            x_start2 = x_end - length + 1
            seq = True
            for j in range(x_start2, x_end + 1):
                if board[y_start][j] != col:
                    seq = False
            if x_start2 != 0:
                if board[y_start][x_start2 - 1] == col:
                    seq = False
            if x_end != len(board[0]) - 1:
                if board[y_start][x_end + 1] == col:
                    seq = False
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMI-OPEN" and seq == True:
                semi_open_seq_count += 1
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN" and seq == True:
                open_seq_count += 1

    if d_y == 1 and d_x == 0:
        x_end = x_start
        for i in range(length - 1, len(board)):
            y_end = i
            y_start2 = y_end - length + 1
            seq = True
            for j in range(y_start2, y_end + 1):
                if board[j][x_start] != col:
                    seq = False
            if y_start2 != 0:
                if board[y_start2 - 1][x_start] == col:
                    seq = False
            if y_end != len(board) - 1:
                if board[y_end + 1][x_start] == col:
                    seq = False
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMI-OPEN" and seq == True:
                semi_open_seq_count += 1
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN" and seq == True:
                open_seq_count += 1

    if d_y == 1 and d_x == 1:
        for i in range(length - 1, len(board) - x_start - y_start):
            x_end = x_start + i
            y_end = y_start + i
            x_start2 = x_end - length + 1
            y_start2 = y_end - length + 1
            seq = True
            for j in range(0, length):
                if board[y_start2 + j][x_start2 + j] != col:
                    seq = False

            if y_start2 != 0 and x_start2 != 0:
                if board[y_start2 - 1][x_start2 - 1] == col:
                    seq = False
            if y_end != len(board) - 1 and x_end != len(board[0]) - 1:
                if board[y_end + 1][x_end + 1] == col:
                    seq = False
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMI-OPEN" and seq == True:
                semi_open_seq_count += 1
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN" and seq == True:
                open_seq_count += 1

    if d_y == 1 and d_x == -1:
        for i in range(length - 1, (x_start + 1) - y_start):
            x_end = x_start - i
            y_end = y_start + i
            x_start2 = x_end + length - 1
            y_start2 = y_end - length + 1
            seq = True
            for j in range(0, length):
                if board[y_start2 + j][x_start2 - j] !=col:
                    seq = False

            if y_start2 != 0 and x_start2 != len(board[0]) - 1:
                if board[y_start2 - 1][x_start2 + 1] == col:
                    seq = False
            if y_end != len(board) - 1 and x_end != 0:
                if board[y_end + 1][x_end - 1] == col:
                    seq = False

            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMI-OPEN" and seq == True:
                semi_open_seq_count += 1
            if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN" and seq == True:
                open_seq_count += 1


    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    '''This function analyses the board board. The function returns a tuple, whose first element is the
number of open sequences of colour col of length lengthon the entire board, and whose second
element is the number of semi-open sequences of colour col of length length on the entire board.'''
    open_seq_count, semi_open_seq_count = 0, 0
    open_seq_count1, semi_open_seq_count1 = 0, 0
    open_seq_count2, semi_open_seq_count2 = 0, 0
    open_seq_count3, semi_open_seq_count3 = 0, 0
    open_seq_count4, semi_open_seq_count4 = 0, 0
    open_seq_count5, semi_open_seq_count5 = 0, 0
    open_seq_count6, semi_open_seq_count6 = 0, 0

    for i in range(0, len(board)):
        open_seq_count1, semi_open_seq_count1 = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += open_seq_count1
        semi_open_seq_count += semi_open_seq_count1

    for j in range(0, len(board[0])):
        open_seq_count2, semi_open_seq_count2 = detect_row(board, col, 0, j, length, 1, 0)
        open_seq_count += open_seq_count2
        semi_open_seq_count += semi_open_seq_count2

        open_seq_count3, semi_open_seq_count3 = detect_row(board, col, 0, j, length, 1, 1)
        open_seq_count += open_seq_count3
        semi_open_seq_count += semi_open_seq_count3

    for k in range(1, len(board)):
        open_seq_count4, semi_open_seq_count4 = detect_row(board, col, k, 0, length, 1, 1)
        open_seq_count += open_seq_count4
        semi_open_seq_count += semi_open_seq_count4

        open_seq_count5, semi_open_seq_count5 = detect_row(board, col, 0, k, length, 1, -1)
        open_seq_count += open_seq_count5
        semi_open_seq_count += semi_open_seq_count5

        open_seq_count6, semi_open_seq_count6 = detect_row(board, col, k, len(board[0]) - 1, length, 1, -1)
        open_seq_count += open_seq_count6
        semi_open_seq_count += semi_open_seq_count6

    return open_seq_count, semi_open_seq_count

def search_max(board):
    '''This function uses the function score() to find the optimal move for black. It finds the
location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of
the board as calculated by score(). The function returns a tuple (y, x) such that putting a black
stone in coordinates (y, x) maximizes the potential score.'''
    score_dict = {}
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == " ":
                board[i][j] = "b"
                coord = i, j
                score_dict[coord] = score(board)
                board[i][j] = " "
    max_coord = max(score_dict, key=score_dict.get)
    move_y, move_x = max_coord

    return move_y, move_x

def score(board):
    '''this function computes and returns the score for the position of the board. It assumes that black has just moved'''

    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def detect_every_row(board, col, y_start, x_start, length, d_y, d_x):
    seq_count = 0
    if d_y == 0 and d_x == 1:
        y_end = y_start
        for i in range(length - 1, len(board[0])):
            x_end = i
            x_start2 = x_end - length + 1
            seq = True
            for j in range(x_start2, x_end + 1):
                if board[y_start][j] != col:
                    seq = False
            if x_start2 != 0:
                if board[y_start][x_start2 - 1] == col:
                    seq = False
            if x_end != len(board[0]) - 1:
                if board[y_start][x_end + 1] == col:
                    seq = False
            if seq == True:
                seq_count += 1


    if d_y == 1 and d_x == 0:
        x_end = x_start
        for i in range(length - 1, len(board)):
            y_end = i
            y_start2 = y_end - length + 1
            seq = True
            for j in range(y_start2, y_end + 1):
                if board[j][x_start] != col:
                    seq = False
            if y_start2 != 0:
                if board[y_start2 - 1][x_start] == col:
                    seq = False
            if y_end != len(board) - 1:
                if board[y_end + 1][x_start] == col:
                    seq = False
            if seq == True:
                seq_count += 1


    if d_y == 1 and d_x == 1:
        for i in range(length - 1, len(board) - x_start - y_start):
            x_end = x_start + i
            y_end = y_start + i
            x_start2 = x_end - length + 1
            y_start2 = y_end - length + 1
            seq = True
            for j in range(0, length):
                if board[y_start2 + j][x_start2 + j] != col:
                    seq = False

            if y_start2 != 0 and x_start2 != 0:
                if board[y_start2 - 1][x_start2 - 1] == col:
                    seq = False
            if y_end != len(board) - 1 and x_end != len(board[0]) - 1:
                if board[y_end + 1][x_end + 1] == col:
                    seq = False
            if seq == True:
                seq_count += 1


    if d_y == 1 and d_x == -1:
        for i in range(length - 1, (x_start + 1) - y_start):
            x_end = x_start - i
            y_end = y_start + i
            x_start2 = x_end + length - 1
            y_start2 = y_end - length + 1
            seq = True
            for j in range(0, length):
                if board[y_start2 + j][x_start2 - j] !=col:
                    seq = False

            if y_start2 != 0 and x_start2 != len(board[0]) - 1:
                if board[y_start2 - 1][x_start2 + 1] == col:
                    seq = False
            if y_end != len(board) - 1 and x_end != 0:
                if board[y_end + 1][x_end - 1] == col:
                    seq = False

            if seq == True:
                seq_count += 1
    return seq_count

def detect_all_rows(board, col, length):
    seq_count = 0
    seq_count1 = 0
    seq_count2 = 0
    seq_count3 = 0
    seq_count4 = 0
    seq_count5 = 0
    seq_count6 = 0

    for i in range(0, len(board)):
        seq_count1 = detect_every_row(board, col, i, 0, length, 0, 1)
        seq_count += seq_count1


    for j in range(0, len(board[0])):
        seq_count2 = detect_every_row(board, col, 0, j, length, 1, 0)
        seq_count += seq_count2


        seq_count3= detect_every_row(board, col, 0, j, length, 1, 1)
        seq_count += seq_count3


    for k in range(1, len(board)):
        seq_count4= detect_every_row(board, col, k, 0, length, 1, 1)
        seq_count += seq_count4


        seq_count5 = detect_every_row(board, col, 0, k, length, 1, -1)
        seq_count += seq_count5


        seq_count6= detect_every_row(board, col, k, len(board[0]) - 1, length, 1, -1)
        seq_count += seq_count6

    return seq_count

def is_win(board):
    '''This function determines the current status of the game, and returns one of
["White won", "Black won", "Draw", "Continue playing"], depending on the current status
on the board. The only situation where "Draw" is returned is when board is full.'''
    draw = True
    if detect_all_rows(board, "w", 5) >= 1:
        return "White won"

    if detect_all_rows(board, "b", 5) >= 1:
        return "Black won"

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                draw = False
    if draw == True:
        return "Draw"

    return "Continue playing"


def print_board(board):
    '''this function prints out the gomuko board'''

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    '''computes the number of open and semi-open sequences of both colors'''
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))



def play_gomoku(board_size):
    ''' this function allows the user to play against a computer on a board of size. This function interacts with the AI engine by calling the function searchMax()'''
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



