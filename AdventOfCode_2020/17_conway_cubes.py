#!/usr/bin/env python3

from copy import deepcopy

def gen_nbrs(cc, state, active_cnt):
    cc_x, cc_y, cc_z = cc
    nbrs = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (cc_x + i, cc_y + j, cc_z + k) != cc:
                    nbrs.append((cc_x + i, cc_y + j, cc_z + k))
                    if (cc_x + i, cc_y + j, cc_z + k) in state.keys():
                        active_cnt[0] += 1

    return nbrs

def gen_nbrs_4d(cc, state, active_cnt):
    cc_x, cc_y, cc_z, cc_w = cc
    nbrs = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for w in range(-1, 2):
                    if (cc_x + i, cc_y + j, cc_z + k, cc_w + w) != cc:
                        nbrs.append((cc_x + i, cc_y + j, cc_z + k, cc_w + w))
                        if (cc_x + i, cc_y + j, cc_z + k, cc_w + w) in state.keys():
                            active_cnt[0] += 1

    return nbrs

def check_nbrs(cc, active_cnt, state, new_state, visited):
    if cc not in visited.keys():
        if cc not in state.keys() and active_cnt[0] == 3:
            new_state[cc] = 1
            active_cnt[0] += 1
        elif cc in state.keys() and (active_cnt[0] != 2 and active_cnt[0] != 3):
            del new_state[cc]
            active_cnt[0] -= 1

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
            active = [0]
            nbrs = gen_nbrs(cc, state, active) if dmns == 3 else gen_nbrs_4d(cc, state, active)
            check_nbrs(cc, active, state, new_state, visited)
            for n in nbrs:
                active = [0]
                n_nbrs = gen_nbrs(n, state, active) if dmns == 3 else gen_nbrs_4d(n, state, active)
                check_nbrs(n, active, state, new_state, visited)

        state = deepcopy(new_state)

    return len(state)

if __name__ == "__main__":
    with open("17.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    print("Part-1: Cubes in active state: {}".format(run_simulation(data_list, 3)))
    print("Part-2: Cubes in active state in 4D: {}".format(run_simulation(data_list, 4)))
