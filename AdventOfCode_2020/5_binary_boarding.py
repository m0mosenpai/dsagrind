#!/usr/bin/env python3

# global dictionary
COMPLETE_ID_DICT = {}

"""
Cool Observation:

Each string in the input can actually just be interpreted as binary where F is 0 and B is 1.
This allows us to calculate entire row number and column number at once by replacing F by 0 and B by 1
and simply converting the resulting binary numers to decimal.
"""

# O(n) Time Complexity | O(n) Space Complexity
def part_1(data_list):
    max_id = 0
    min_id = float("inf")

    for data in data_list:
        row_part = data[:7]
        col_part = data[7:]
        _max_row, _max_col = 127, 7
        _min_row, _min_col = 0, 0

        for letter in row_part:
            if letter == "B":
                _min_row = (_min_row + _max_row) // 2 + 1
            elif letter == "F":
                _max_row = (_min_row + _max_row) // 2

        for letter in col_part:
            if letter == "R":
                _min_col = (_min_col + _max_col) // 2 + 1
            elif letter == "L":
                _max_col = (_min_col + _max_col) // 2

        final_row, final_col = min(_min_row, _max_row), max(_min_col, _max_col)
        seat_id = (final_row * 8) + final_col
        COMPLETE_ID_DICT[seat_id] = data

        if seat_id > max_id:
            max_id = seat_id

        if seat_id < min_id:
            min_id = seat_id

    print(f"Max Seat ID: {max_id}")
    print(f"Min Seat ID: {min_id}")
    return (min_id, max_id)


# O(n) Time Complexity | O(1) Space Complexity
def part_2(data_list, min_id, max_id):
    for _id in range(min_id + 1, max_id):
        current = COMPLETE_ID_DICT.get(_id, None)
        _prev = COMPLETE_ID_DICT.get(_id - 1, None)
        _next = COMPLETE_ID_DICT.get(_id + 1, None)

        if current is None and _prev is not None and _next is not None:
            print(f"My ID: {_id}")
            break


if __name__ == "__main__":
    with open("5.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    min_id, max_id = part_1(data_list)
    part_2(data_list, min_id, max_id)
