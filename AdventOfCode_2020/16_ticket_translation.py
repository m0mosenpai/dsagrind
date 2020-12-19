#!/usr/bin/env python3

# global
NEW_LIST = []

# O(n^2) Time Complexity | O(n) Space Complexity
def part_1(data_list):
    cd = []
    for data in data_list:
        if data == "":
            break

        ranges = data.split(": ")[1].split(" or ")
        p_1 = (int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]))
        p_2 = (int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]))
        cd.append(p_1)
        cd.append(p_2)

    points = {}
    cd.sort()
    last_end = cd[0][1]
    _max, _min = cd[0][1], cd[0][0]

    for i in range(1, len(cd)):
        if cd[i][1] > _max:
            _max = cd[i][1]

        if last_end < cd[i][0]:
            for j in range(last_end + 1, cd[i][0]):
                points[j] = 0

        last_end = cd[i][1]

    invalid_sum = 0
    global NEW_LIST
    for i, data in enumerate(reversed(data_list)):
        is_invalid = False
        if data.startswith("nearby"):
            break

        for val in data.split(","):
            if points.get(int(val), None) == 0 or int(val) > _max or int(val) < _min:
                invalid_sum += int(val)
                is_invalid = True

        if not is_invalid:
            NEW_LIST.append(data)

    return invalid_sum

# O(n^2) Time Complexity | O(n) Space Complexity
# Messy code. Should be a better way to do this.
def part_2(data_list):
    cd = []
    field_end = None
    for i, data in enumerate(data_list):
        if data == "":
            field_end = i
            break

        ranges = data.split(": ")[1].split(" or ")
        cd.append((int(ranges[0].split("-")[1]) + 1, int(ranges[1].split("-")[0]) - 1))

    arrangement_dict = {}
    final_list = []

    for i, data in enumerate(NEW_LIST):
        val_list = list(map(int, data.split(",")))
        tmp_dict = {}
        for j, val in enumerate(val_list):
            for k, field in enumerate(cd):
                if val < cd[k][0] or val > cd[k][1]:
                    if j in tmp_dict.keys():
                        tmp_dict[j].append(k)
                    else:
                        tmp_dict[j] = [k]

        final_list.append(tmp_dict)

    for i in range(len(cd)):
        fields = [val[i] for val in final_list]
        arrangement_dict[i] = list(set.intersection(*[set(x) for x in fields]))

    arrangement_dict = dict(sorted(arrangement_dict.items(), key= lambda item: len(item[1])))
    assigned = []
    for key, val in arrangement_dict.items():
        for avs in assigned:
            val.remove(avs)
        arrangement_dict[key] = val[0]
        assigned.append(val[0])

    prod = 1
    my_ticket = list(map(int, data_list[field_end + 2].split(",")))
    for key, val in arrangement_dict.items():
        if val < 6:
            prod *= my_ticket[key]

    return prod

if __name__ == "__main__":
    with open("16.txt", "r") as f:
        data = f.read()

    data_list = data.strip().split("\n")

    print("Invalid Sum: {}".format(part_1(data_list)))
    print("Product of departures: {}".format(part_2(data_list)))
