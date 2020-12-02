#!/usr/bin/env python3

# O(n*m) Time Complexity | O(1) Space Complexity [O(n) if you consider input array]
def part_1(data_list):
	invalid_passwords = 0
	for data in data_list:
		policy, password = data.split(": ")[0], data.split(": ")[1]
		_range, letter = policy.split()[0], policy.split()[1]
		_min, _max = int(_range.split("-")[0]), int(_range.split("-")[1])

		letter_count = 0
		for c in password:
			if c == letter:
				letter_count += 1

		if letter_count < _min or letter_count > _max:
			invalid_passwords += 1

	print(f"Invalid Password Count: {invalid_passwords}")
	print(f"Valid Password Count: {len(data_list) - invalid_passwords}")

# O(n) Time Complexity | O(1) Space Complexity [O(n) if you consider input array]
def part_2(data_list):
	invalid_passwords = 0
	for data in data_list:
		policy, password = data.split(": ")[0], data.split(": ")[1]
		positions, letter = policy.split()[0], policy.split()[1]
		pos_1, pos_2 = int(positions.split("-")[0]), int(positions.split("-")[1])

		if password[pos_1 - 1] == letter and password[pos_2 - 1] == letter:
			invalid_passwords += 1
		elif password[pos_1 - 1] != letter and password[pos_2 - 1] != letter:
			invalid_passwords += 1

	print(f"Invalid Password Count: {invalid_passwords}")
	print(f"Valid Password Count: {len(data_list) - invalid_passwords}")

if __name__ == '__main__':
	with open("2.txt", "r") as f:
		data = f.read()

	data_list = data.strip().split("\n")

	print("Part-1:")
	part_1(data_list)
	print()
	print("Part-2")
	part_2(data_list)