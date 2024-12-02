from collections import Counter


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


def calc_similarity_score(list1: list[int], list2: list[int]) -> int:

    total_sim_score = 0
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    for key, val in counter1.items():
        # sim score is value of number * count in list1 * count in list2
        total_sim_score += key * val * counter2.get(key, 0)
    return total_sim_score


def main():
    filename = "aoc-dec1-input.txt"
    list1, list2 = load_input_lists(filename)
    list1.sort()
    list2.sort()
    total_sim_score = calc_similarity_score(list1, list2)
    print(f"Total Similarity Score: {total_sim_score}")


if __name__ == "__main__":
    main()
