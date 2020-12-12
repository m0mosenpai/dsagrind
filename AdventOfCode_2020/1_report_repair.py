#!/usr/bin/env python3

# O(nlog n) Time Complexity | O(1) Space complexity
# Best sorting algorithm would take O(nlog n)
def part_1(data_list):
    start = 0
    end = len(data_list) - 1
    _sum = 0

    while start < end:
        _sum = data_list[start] + data_list[end]

        if _sum < 2020:
            start += 1
        elif _sum > 2020:
            end -= 1
        else:
            print(
                f"{data_list[start]} + {data_list[end]} = {_sum}. Product = {data_list[start]*data_list[end]}"
            )
            exit(0)


# O(n^2) Time Complexity | O(1) Space Complexity
# Best sorting algorithm would take O(nlog n)
def part_2(data_list):
    for start in range(len(data_list)):
        mid = start + 1
        end = len(data_list) - 1
        _sum = 0

        while mid <= end:
            _sum = data_list[start] + data_list[mid] + data_list[end]
            if _sum < 2020:
                mid += 1
            elif _sum > 2020:
                end -= 1
            else:
                print(
                    f"{data_list[start]} + {data_list[mid]} + {data_list[end]} = {_sum}. Product = {data_list[start]*data_list[mid]*data_list[end]}"
                )
                exit(0)


if __name__ == "__main__":
    with open("1.txt", "r") as f:
        data = f.read()

    data_list = list(map(int, data.strip().split("\n")))
    data_list.sort()

    part_1(data_list)
    part_2(data_list)
