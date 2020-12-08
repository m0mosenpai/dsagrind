#!/usr/bin/env python3

# global
JMP_OR_NOP = []

# O(n) Time Complexity | O(m) Space Complexity [where n is max length of one execution loop, m is length of input]
def part_1(data_list):
	executed = [0 for i in range(len(data_list))]
	ip = 0
	acc = 0

	while True:
		if ip >= len(data_list):
			print("Exited Successfully!")
			print(f"Accumulator Value: {acc}")
			return True

		if executed[ip] == 1:
			break

		executed[ip] = 1
		if data_list[ip].split(" ")[0] == "nop":
			JMP_OR_NOP.append(ip)
			ip += 1
		elif data_list[ip].split(" ")[0] == "acc":
			acc += int(data_list[ip].split(" ")[1])
			ip += 1
		elif data_list[ip].split(" ")[0] == "jmp":
			JMP_OR_NOP.append(ip)
			ip += int(data_list[ip].split(" ")[1])

	return False

# O(n*k) Time Complexity | O(m + k) Space Complexity [where k is the number of jmp + nop instructions, m is length of input]
def part_2(data_list):
	for ins in JMP_OR_NOP:
		tmp_data_list = data_list[:]
		if data_list[ins].split(" ")[0] == "nop":
			data_list[ins] = "jmp {}".format(data_list[ins].split(" ")[1])
		elif data_list[ins].split(" ")[0] == "jmp":
			data_list[ins] = "nop {}".format(data_list[ins].split(" ")[1])

		if part_1(data_list):
			break
		data_list = tmp_data_list

if __name__ == '__main__':
	with open("8.txt", "r") as f:
		data = f.read()

	data_list = data.strip().split("\n")

	part_1(data_list)
	part_2(data_list)