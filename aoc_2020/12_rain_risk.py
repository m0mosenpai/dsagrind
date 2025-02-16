#!/usr/bin/env python3
from copy import deepcopy

# globals
ROTATIONS = {
    "N": {"L": "W", "R": "E"},
    "W": {"L": "S", "R": "N"},
    "S": {"L": "E", "R": "W"},
    "E": {"L": "N", "R": "S"},
}


def opposite_of(current_dir):
    opposites = {"N": "S", "W": "E", "E": "W", "S": "N"}
    return opposites[current_dir]


def change_rotation(direction, value, position):
    facing = position["F"]

    rot_cnt = value // 90
    for _ in range(rot_cnt):
        facing = ROTATIONS[facing][direction]

    position["F"] = facing


def update_status(direction, value, position):
    updated_value = position[direction] + value - position[opposite_of(direction)]
    updated_value_opp = position[opposite_of(direction)] - value
    position[direction] = updated_value if updated_value > 0 else 0
    position[opposite_of(direction)] = updated_value_opp if updated_value_opp > 0 else 0


def rotate_waypoint(direction, value, position):
    rot_cnt = value // 90

    tmp_position = {"N": 0, "W": 0, "E": 0, "S": 0}
    for _dir in position:
        if position[_dir] != 0:
            new_dir = _dir
            for _ in range(rot_cnt):
                new_dir = ROTATIONS[new_dir][direction]

            tmp_position[new_dir] = position[_dir]

    position = deepcopy(tmp_position)
    return position


def update_ship_position(value, ship_pos, waypoint_pos):
    for pos in ship_pos:
        ship_pos[pos] += value * waypoint_pos[pos]

    NS_diff = ship_pos["N"] - ship_pos["S"]
    EW_diff = ship_pos["E"] - ship_pos["W"]
    ship_pos["N"] = NS_diff if NS_diff > 0 else 0
    ship_pos["S"] = abs(NS_diff) if NS_diff < 0 else 0
    ship_pos["E"] = EW_diff if EW_diff > 0 else 0
    ship_pos["W"] = abs(EW_diff) if EW_diff < 0 else 0


# O(n) Time Complexity | O(1) Space Complexity
def part_1(data_list):
    position = {"N": 0, "W": 0, "E": 0, "S": 0, "F": "E"}

    for count, ins in enumerate(data_list):
        direction = position["F"] if ins[0] == "F" else ins[0]
        value = int(ins[1:])
        if direction == "L" or direction == "R":
            change_rotation(direction, value, position)
        else:
            update_status(direction, value, position)

    _sum = 0
    for pos in list(position.keys())[:-1]:
        _sum += position[pos]

    return _sum


# O(n) Time Complexity | O(1) Space Complexity
def part_2(data_list):
    waypoint_position = {"N": 1, "W": 0, "E": 10, "S": 0}

    ship_position = {"N": 0, "W": 0, "E": 0, "S": 0}

    for count, ins in enumerate(data_list):
        direction = ins[0]
        value = int(ins[1:])
        if direction == "F":
            update_ship_position(value, ship_position, waypoint_position)
        elif direction == "L" or direction == "R":
            waypoint_position = rotate_waypoint(direction, value, waypoint_position)
        else:
            update_status(direction, value, waypoint_position)

    _sum = 0
    for pos in ship_position.keys():
        _sum += ship_position[pos]

    return _sum


if __name__ == "__main__":
    with open("12.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    print("Manhattan Distance: {}".format(part_1(data_list)))
    print("Manhattan Distance with correct instructions: {}".format(part_2(data_list)))
