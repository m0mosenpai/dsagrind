#!/usr/bin/env python3

# global
GROUP_SIZES = []

# O(n) Time Complexity | O(n) Space Complexity
def part_1(data_list):
    yes_count = 0
    total = 0
    group_size = 0
    questions = [0 for i in range(26)]
    for data in data_list:
        if data == "":
            yes_count = 0
            questions = [0 for i in range(26)]
            GROUP_SIZES.append(group_size)
            group_size = 0
            continue

        group_size += 1
        for letter in data:
            pos = ord(letter) - 97
            if questions[pos] != 1:
                questions[pos] = 1
                yes_count += 1
                total += 1

    print(f"Sum of Counts: {total}")


# O(n) Time Complexity | O(1) Space Complexity
def part_2(data_list):
    yes_count = 0
    total = 0
    size_idx = 0
    questions = [0 for i in range(26)]
    for data in data_list:
        if data == "":
            for count in questions:
                if count == GROUP_SIZES[size_idx]:
                    total += 1

            questions = [0 for i in range(26)]
            size_idx += 1

        for letter in data:
            pos = ord(letter) - 97
            questions[pos] += 1

    print(f"Sum of counts to questions answered by everyone: {total}")


if __name__ == "__main__":
    with open("6.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    part_1(data_list)
    part_2(data_list)
