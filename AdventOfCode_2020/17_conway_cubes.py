#!/usr/bin/env python3

def get_active_count(neighbors, state):
    count_active = 0
    for n in neighbors:
        x, y, z = n
        if (x, y, z) in state.keys():
            count_active += 1

    return count_active

def generate_neighbors(cc):
    cc_x, cc_y, cc_z = cc
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (i, j, k) != cc:
                    neighbors.append((cc_x + i, cc_y + j, cc_z + k))

    return neighbors

def check_neighbors(cc, state, new_state):
    neighbors = generate_neighbors(cc)
    count_active = get_active_count(neighbors, state)

    if (cc_x, cc_y, cc_z) not in state.keys() and count_active == 3:
        new_state[(cc_x, cc_y, cc_z)] = 1
    elif (cc_x, cc_y, cc_z) in state.keys() and (count_active == 2 or count_active == 3):
        new_state[(cc_x, cc_y, cc_z)] == 1

def part_1(data_list):
    state, new_state = {}, {}
    z = 0
    for i, row in enumerate(data_list):
        for j, col in enumerate(row):
            if data_list[i][j] == "#":
                state[(i, j, z)] = 1

    for cc, val in state.items():
        check_neighbors(cc, state, new_state)



def part_2(data_list):
    pass

if __name__ == "__main__":
    with open("17.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    part_1(data_list)
    part_2(data_list)
