#!/usr/bin/env python3


def scuffed_dfs(root, data_dict):
    for n in data_dict[root]:
        if n[0] == "shiny gold":
            return True
        if scuffed_dfs(n[0], data_dict):
            return True

    return False


# O(n*V) Time Complexity | O(V) Space Complexity [where V is number of vertices]
def part_1(data_dict):
    count = 0
    for i, node in enumerate(data_dict.keys()):
        if scuffed_dfs(node, data_dict):
            count += 1

    return count


# O(V) Time Complexity | O(h) Space Complexity [where V is vertices and h is max recursive depth]
def part_2(node, data_dict):
    total = 0
    for n in data_dict[node]:
        total += int(n[1]) + (int(n[1]) * part_2(n[0], data_dict))

    return total


if __name__ == "__main__":
    with open("7.txt", "r") as f:
        data = f.read()

    data_dict = {}
    data_list = data.strip().split("\n")
    for i in range(len(data_list)):
        bag_list = []
        data_list[i] = (
            data_list[i]
            .replace("contain", "->")
            .replace("bags", "")
            .replace("bag", "")
            .replace(" .", "")
        )
        for j in data_list[i].split(" -> ")[1].split(" , "):
            bag_name = j[2:]
            if bag_name != " other":
                bag_list.append((bag_name, j[0]))
        data_dict[data_list[i].split(" -> ")[0].strip()] = bag_list

    print("Count: {}".format(part_1(data_dict)))
    print("Bags in shiny gold: {}".format(part_2("shiny gold", data_dict)))
