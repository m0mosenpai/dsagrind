#!/usr/bin/env python3

# O(n) Time Complexity [where n = number of rows] | O(1) Space Complexity
def part_1(data_list):
	i = 0
	j = 0
	trees = 0
	while i < len(data_list):
		if j > len(data_list[0]) - 1:
			j = j % len(data_list[0])

		if data_list[i][j] == "#":
			trees += 1

		j += 3
		i += 1

	return trees

# Same algorithm as part-1, just generalized to calculate any path
# O(n*m) Time Complexity [where n = number of rows, m = number of inputs] | O(1) Space Complexity
def part_2(data_list, x, y):
	i = 0
	j = 0
	trees = 0
	while i < len(data_list):
		j = j % len(data_list[0])

		if data_list[i][j] == "#":
			trees += 1

		j += x
		i += y

	return trees

if __name__ == '__main__':
	with open("3.txt", "r") as f:
		data = f.read()

	data_list = data.strip().split("\n")

	part_2_inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	product = 1
	for i in part_2_inputs:
		x, y = i
		product *= part_2(data_list, x, y)

	print(part_1(data_list))
	print(f"Product of number of trees: {product}")