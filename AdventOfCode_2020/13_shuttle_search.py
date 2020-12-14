#!/usr/bin/env python3.9
import math

# Straightforward Bruteforce
def part_1(data_list):
	min_departure_time = int(data_list[0])
	bus_list = list(map(int, list(filter(lambda x: x != "x", data_list[1].split(",")))))
	rem_dict = {}

	for i, bus in enumerate(bus_list):
		time = min_departure_time
		while (time % bus):
			time += 1
		rem_dict[bus] = (time - min_departure_time)

	rem_dict_sorted = dict(sorted(rem_dict.items(), key=lambda item: item[1]))
	bus_id = list(rem_dict_sorted.keys())[0]
	min_to_departure = rem_dict_sorted[bus_id]

	return bus_id * min_to_departure

# Got to know about the Chinese Remainder Theorem - couldn't figure out on my own this time.
def part_2(data_list):
	cleaned_input = [(int(i),j) for j,i in enumerate(data_list[1].split(',')) if i != 'x']
	
	t, step =0, 1
	for m, d in cleaned_input:
		while (t + d) % m != 0:
			t += step
		step *= m

	return t


if __name__ == "__main__":
    with open("13.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    print("Product: {}".format(part_1(data_list)))
    print(("Using Chinese Remainder Theorem: {}".format(part_2(data_list))))