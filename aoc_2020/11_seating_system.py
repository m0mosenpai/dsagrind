#!/usr/bin/env python3.9
from copy import deepcopy

def neighbors(row, col, seats):
	max_col = len(seats[0])
	max_row = len(seats)

	neighbor_list = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
					 (row, col - 1),					 (row, col + 1),
					 (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

	current_neighbors = list(filter(lambda p: p[0] >= 0 and p[0] < max_row and p[1] >= 0 and p[1] < max_col, neighbor_list))
	return list(filter(lambda x: seats[x[0]][x[1]] == "#", current_neighbors))

def fill_seat(row, col, seats):
	seats[row][col] = "#"

def empty_seat(row, col, seats):
	seats[row][col] = "L"

# O(n^2) Time Complexity | O(n^2) Space Complexity
def part_1(data_list):
	data_list_tmp = deepcopy(data_list)

	total_occupied_seats = 0
	while True:
		state_changed = False
		for rownum, row in enumerate(data_list):
			for colnum, col in enumerate(row):
				occupied_neighbor_cnt = len(neighbors(rownum, colnum, data_list))

				if col == "L" and occupied_neighbor_cnt == 0:
					fill_seat(rownum, colnum, data_list_tmp)
					total_occupied_seats += 1
					state_changed = True
				elif col == "#" and occupied_neighbor_cnt >= 4:
					empty_seat(rownum, colnum, data_list_tmp)
					total_occupied_seats -= 1
					state_changed = True

		data_list = deepcopy(data_list_tmp)
		if not state_changed:
			break

	return total_occupied_seats

def visible_seats(row, col, seats):
    directions = {
        'NW': lambda row, col, delta: (row - delta, col - delta),
        'N': lambda row, col, delta: (row - delta, col),
        'NE': lambda row, col, delta: (row - delta, col + delta),
        'W': lambda row, col, delta: (row, col - delta),
        'E': lambda row, col, delta: (row, col + delta),
        'SW': lambda row, col, delta: (row + delta, col - delta),
        'S': lambda row, col, delta: (row + delta, col),
        'SE': lambda row, col, delta: (row + delta, col + delta),
    }
 
    def is_valid(row, col):
        max_col = len(seats[0])
        max_row = len(seats)
        
        return row in range(0, max_row) and col in range(0, max_col)
 
    visible = []
    delta = 1
    while dirs := list(directions):
        for d in dirs:
            nr, nc = directions[d](row, col, delta)
            if not is_valid(nr, nc):
                del directions[d]
            elif seats[nr][nc] == 'L':
                del directions[d]
            elif seats[nr][nc] == '#':
                visible.append((nr, nc))
                del directions[d]
        delta += 1
    return visible

def part_2(data_list):
	data_list_tmp = deepcopy(data_list)

	total_occupied_seats = 0
	while True:
		state_changed = False
		for rownum, row in enumerate(data_list):
			for colnum, col in enumerate(row):
				viscount = len(visible_seats(rownum, colnum, data_list))
				if col == "L" and viscount == 0:
					fill_seat(rownum, colnum, data_list_tmp)
					total_occupied_seats += 1
					state_changed = True
				elif col == "#" and viscount >= 5:
					empty_seat(rownum, colnum, data_list_tmp)
					total_occupied_seats -= 1
					state_changed = True

		data_list = deepcopy(data_list_tmp)
		if not state_changed:
			break

	return total_occupied_seats


if __name__ == '__main__':
	data_list = []
	with open("11.txt", "r") as f:
		for line in f:
			line = line.rstrip()
			data_list.append(list(line))

	print("Final number of seats occupied: {}".format(part_1(data_list)))
	print("Final number of seats occupied (Part-2): {}".format(part_2(data_list)))