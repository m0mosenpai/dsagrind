#!/usr/bin/env python3

# O(n) Time Complexity | O(1) Space Complexity
def part_1(data_list):
	begin_preamble = 0
	end_preamble = 25

	for i in range(25, len(data_list)):
		current_preamble = data_list[begin_preamble:end_preamble]
		current_preamble.sort()

		start = 0
		end = len(current_preamble) - 1
		_sum = 0

		while start < end:
			_sum = current_preamble[start] + current_preamble[end]

			if _sum < data_list[i]:
				start += 1
			elif _sum > data_list[i]:
				end -= 1
			else:
				break

		if end <= start:
			print("Sum not found! ({})".format(data_list[i]))
			return data_list[i]

		begin_preamble += 1
		end_preamble += 1

# O(n^2) Time Complexity | O(1) Space Complexity
def part_2(data_list, invalid_num):
	for i, num in enumerate(data_list):
		_sum = 0
		_min = num
		_max = num
		for j in range(i, len(data_list)):
			if data_list[j] < _min:
				_min = data_list[j]

			if data_list[j] > _max:
				_max = data_list[j]

			_sum += data_list[j]
			if _sum == invalid_num:
				return (_min + _max)
			elif _sum > invalid_num:
				break

	return -1

if __name__ == '__main__':
	with open("9.txt", "r") as f:
		data = f.read()

	data_list = list(map(int, data.strip().split("\n")))

	invalid_num = part_1(data_list)
	print(part_2(data_list, invalid_num))