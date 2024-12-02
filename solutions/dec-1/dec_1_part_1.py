def load_input_lists(filename: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    with open(filename) as file:
        for line in file:
            locations = line.split()
            loc1 = int(locations[0])
            loc2 = int(locations[1])
            list1.append(loc1)
            list2.append(loc2)

    return list1, list2


def calc_total_distance(list1: list[int], list2: list[int]) -> int:
    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])
    return total_distance


def main():
    filename = "aoc-dec1-input.txt"
    list1, list2 = load_input_lists(filename)
    list1.sort()
    list2.sort()
    total_dist = calc_total_distance(list1, list2)
    print(f"Total Distance Between Lists: {total_dist}")


if __name__ == "__main__":
    main()
