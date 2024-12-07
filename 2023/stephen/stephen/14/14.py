# python 1.py input.txt
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()
with open(args.input_file, 'r') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()


def calculate_weight(row):
    row_total = 0
    row_length = len(row)
    row_weight = row_length
    for i in range(row_length):
        if row[i] == 0:
            continue

        if row[i] == 1:
            row_total += row_weight
            row_weight -= 1

        if row[i] == -1:
            row_weight = row_length - (i + 1)

    return row_total


def tilt_board(board):
    tilted_board = []

    for row in board:
        tilted_board.append(sort_row(row))

    return tilted_board


def sort_row(row):
    sorted_row = []
    i = 0
    for i in range(len(row)):
        if row[i] == 0:
            continue
        if row[i] == 1:
            sorted_row.append(1)
        if row[i] == -1:
            for n in range(i - len(sorted_row)):
                sorted_row.append(0)
            sorted_row.append(-1)
        i += 1

    if len(sorted_row) < len(row):
        for n in range(len(row) - len(sorted_row)):
            sorted_row.append(0)

    return sorted_row


def rotate_board_90(board):
    new_board = []
    board_length = len(board)
    row_length = len(board[0])

    for n in range(row_length):
        new_board.append([])

    for i in range(board_length):
        for j in range(len(board[i])):
            new_board[-j-1].append(board[i][j])

    return new_board


if __name__ == "__main__":
    raw_array = []
    for line in lines:
        raw_array.append([])
        for i in range(len(line)):
            if line[i] == '.':
                raw_array[-1].append(0)
            if line[i] == 'O':
                raw_array[-1].append(1)
            if line[i] == '#':
                raw_array[-1].append(-1)

    array = np.array(raw_array)
    array_T = array.T
    columns = array_T.tolist()

    board = array.tolist()

    for row in board:
        print(row)

    num_rotations = 1000000000 * 4

    board = tilt_board(board)
    
    for n in range(num_rotations):
        board = rotate_board_90(board)
        board = tilt_board(board)

    board = rotate_board_90(board)

    weight = 0

    for row in board:
        weight += calculate_weight(row)


    '''
    # part 1
    total_weight = 0
    for row in columns:
        total_weight += calculate_weight(row)

    print(total_weight)
    '''

