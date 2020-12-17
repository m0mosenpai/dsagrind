#!/usr/bin/env python3.9

# 0, 3, 6
# count[0] = [2, {1, 4}]
# count[3] = [1, {None, 2}]
# count[6] = [1, {None, 3}]
#

# global
PUZZLE_INPUT = [20, 0, 1, 11, 6, 3]

def set_new_count(num, turn, count):
    count[num] = [1, {"last_to_last": None, "last": turn}]


def update_count(num, turn, count):
    count[num][0] += 1
    count[num][1]["last_to_last"] = count[num][1]["last"]
    count[num][1]["last"] = turn


def get_new_number(num, count):
    return count[num][1]["last"] - count[num][1]["last_to_last"]


def part_1():
    turn = 0
    count = {}
    last_num = None

    while True:
        turn += 1
        if turn == 2021:
            print(f"2020th Number: {last_num}")

        if turn == 30000001:
            return last_num

        if turn <= len(PUZZLE_INPUT):
            last_num = PUZZLE_INPUT[turn - 1]
        else:
            last_num = 0 if count[last_num][0] == 1 else get_new_number(last_num, count)

        if last_num not in count.keys():
            set_new_count(last_num, turn, count)
        else:
            update_count(last_num, turn, count)

if __name__ == "__main__":
    print("30000000th Turn - last number: {}".format(part_1()))
