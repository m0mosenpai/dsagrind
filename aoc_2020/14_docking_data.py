#!/usr/bin/env python3.9
import re

def indices(newidx, floating):
	if len(floating) == 0:
		return [newidx]
	else:
		b0 = floating.pop(0)
		ans = indices(newidx, list(floating)) + indices(newidx + 2**b0, list(floating))
		return ans

def modify_idx(idx, mask):
	newidx = 0
	floating = []
	for i, bit in enumerate(reversed(mask)):
		ibit = idx & (2**i)
		if bit == "X":
			floating.append(i)
		elif bit == "1":
			newidx += 2**i
		elif bit == "0":
			newidx += ibit
			pass
		else:
			assert False

	return indices(newidx, list(floating))

def part_1(data_list):
	memory = {}
	mask = '0' * 36
	

	for data in data_list:
		ins = data.split(" = ")[0]
		value = data.split(" = ")[1]

		if ins == "mask":
			mask = value
		else:
			mem_location = re.search(r"\[([0-9]+)\]", ins).group(1)
			bin_value = "{0:036b}".format(int(value))
			padded_bin_list = [dig for dig in bin_value]

			for i, val in enumerate(mask):
				if val != "X":
					padded_bin_list[i] = mask[i]

			memory[mem_location] = int(''.join(padded_bin_list), 2)

	return sum(memory.values())

def part_1_bitwise(data_list):
	memory = {}
	mask = '0' * 36
	or_mask = 0
	and_mask = -1

	for data in data_list:
		ins, value = data.split(" = ")[0], data.split(" = ")[1]

		if ins == "mask":
			mask = value
			or_mask = int(value.replace("X", "0"), 2)
			and_mask = int(value.replace("X", "1"), 2)
		else:
			mem_location = re.search(r"\[([0-9]+)\]", ins).group(1)
			memory[mem_location] = int(value) & and_mask | or_mask

	return sum(memory.values())

def part_2(data_list):
	memory = {}
	mask = '0' * 36
	or_mask = 0

	for data in data_list:
		ins, value = data.split(" = ")[0], data.split(" = ")[1]

		if ins == "mask":
			mask = value
		else:
			mem_location = int(re.search(r"\[([0-9]+)\]", ins).group(1))
			I = [mem_location]
			I = modify_idx(mem_location, mask)

			for idx2 in I:
				memory[idx2] = int(value)

	return sum(memory.values())

if __name__ == "__main__":
    with open("14.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    print("Sum Of all values in memory: {}".format(part_1(data_list)))
    print("Sum Of all values in memory using bitwise: {}".format(part_1_bitwise(data_list)))
    print("Sum of all values in memory if floating addresses: {}".format(part_2(data_list)))