#!/usr/bin/env python3


def part_1(final_list):
    all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    valid = 0
    valid_list = []
    for passport in final_list:
        if len(passport.keys()) == len(all_keys):
            valid_list.append(passport)
            valid += 1
        elif len(passport.keys()) == len(all_keys) - 1:
            cid = passport.get("cid", None)
            if cid is None:
                valid_list.append(passport)
                valid += 1

    return valid_list


def part_2(final_list):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid_list = part_1(final_list)

    valid = 0
    for passport in valid_list:
        if (
            len(passport["byr"]) != 4
            or int(passport["byr"]) < 1920
            or int(passport["byr"]) > 2002
        ):
            continue
        try:
            int(passport["byr"])
        except ValueError:
            continue

        if (
            len(passport["iyr"]) != 4
            or int(passport["iyr"]) < 2010
            or int(passport["iyr"]) > 2020
        ):
            continue
        try:
            int(passport["iyr"])
        except ValueError:
            continue

        if (
            len(passport["eyr"]) != 4
            or int(passport["eyr"]) < 2020
            or int(passport["eyr"]) > 2030
        ):
            continue
        try:
            int(passport["eyr"])
        except ValueError:
            continue

        try:
            int(passport["hgt"][:-2])
        except ValueError:
            continue

        if passport["hgt"][-2:] == "cm":
            if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
                continue
        elif passport["hgt"][-2:] == "in":
            if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
                continue
        else:
            continue

        if passport["hcl"][0] != "#" or len(passport["hcl"][1:]) != 6:
            continue
        try:
            int(passport["hcl"][1:], 16)
        except ValueError as e:
            continue

        if passport["ecl"] not in eye_colors:
            continue

        if len(passport["pid"]) != 9:
            continue
        try:
            int(passport["pid"])
        except ValueError as e:
            continue

        valid += 1

    print(f"Final Valid Passports: {valid}")


if __name__ == "__main__":
    with open("4.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")
    final_list = []
    tmp_dict = {}
    for data in data_list:
        if data == "":
            final_list.append(tmp_dict)
            tmp_dict = {}
            continue

        for field in data.split(" "):
            tmp_dict[field.split(":")[0]] = field.split(":")[1]

    part_2(final_list)
