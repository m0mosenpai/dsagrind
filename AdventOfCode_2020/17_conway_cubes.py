#!/usr/bin/env python3

from copy import deepcopy

def get_active_count(neighbors, state):
    count_active = 0
    for n in neighbors:
        if n in state.keys():
            count_active += 1

    return count_active

def generate_neighbors(cc):
    cc_x, cc_y, cc_z = cc
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (cc_x + i, cc_y + j, cc_z + k) != cc:
                    neighbors.append((cc_x + i, cc_y + j, cc_z + k))

    return neighbors

def generate_neighbors_4d(cc):
    cc_x, cc_y, cc_z, cc_w = cc
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for w in range(-1, 2):
                    if (cc_x + i, cc_y + j, cc_z + k, cc_w + w) != cc:
                        neighbors.append((cc_x + i, cc_y + j, cc_z + k, cc_w + w))

    return neighbors

def check_neighbors(cc, state, new_state, neighbors, visited):
    if cc not in visited.keys():
        active = get_active_count(neighbors, state)

        if cc not in state.keys() and active == 3:
            new_state[cc] = 1
        elif cc in state.keys() and (active != 2 and active != 3):
            del new_state[cc]

        visited[cc] = 1

def get_active_states(data_list, dmns):
    state = {}
    z, w = 0, 0
    for i, row in enumerate(data_list):
        for j, col in enumerate(row):
            if data_list[i][j] == "#":
                if dmns == 3:
                    state[(i, j, z)] = 1
                elif dmns == 4:
                    state[(i, j, z, w)] = 1
                else:
                    assert False

    return state

def run_simulation(data_list, dmns):
    state = get_active_states(data_list, dmns)

    new_state = deepcopy(state)
    for _ in range(6):
        visited = {}
        for cc, val in state.items():
            neighbors = generate_neighbors(cc) if dmns == 3 else generate_neighbors_4d(cc)
            check_neighbors(cc, state, new_state, neighbors, visited)
            for n in neighbors:
                n_neighbors = generate_neighbors(n) if dmns == 3 else generate_neighbors_4d(n)
                check_neighbors(n, state, new_state, n_neighbors, visited)

        state = deepcopy(new_state)

    return len(state)

if __name__ == "__main__":
    with open("17.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    print("Part-1: Cubes in active state: {}".format(run_simulation(data_list, 3)))
    print("Part-2: Cubes in active state in 4D: {}".format(run_simulation(data_list, 4)))
