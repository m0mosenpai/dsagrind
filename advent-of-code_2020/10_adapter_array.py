#!/usr/bin/env python3

# O(n) Time Complexity | O(1) Space Complexity
def part_1(data_list):
    one_jolt_diff = 0
    three_jolt_diff = 0

    for i in range(len(data_list) - 1):
        if data_list[i + 1] - data_list[i] == 1:
            one_jolt_diff += 1
        elif data_list[i + 1] - data_list[i] == 3:
            three_jolt_diff += 1

    three_jolt_diff += 1
    one_jolt_diff += 1
    print(
        "{} x {} = {}".format(
            three_jolt_diff, one_jolt_diff, three_jolt_diff * one_jolt_diff
        )
    )


# O(n) Time Compelexity | O(n) Space Complexity
def part_2(data_list):
    dp = [0 for i in range(data_list[-1] + 1)]
    exists = [0 for i in range(data_list[-1] + 1)]
    for num in data_list:
        exists[num] = 1

    dp[0] = 1
    dp[1] = exists[1]
    dp[2] = dp[0] + dp[1]

    for i in range(3, len(dp)):
        if exists[i] == 1:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[-1]


if __name__ == "__main__":
    with open("10.txt", "r") as f:
        data = f.read()

    data_list = list(map(int, data.strip().split("\n")))
    data_list.sort()

    part_1(data_list)
    print("Number of different paths: {}".format(part_2(data_list)))
