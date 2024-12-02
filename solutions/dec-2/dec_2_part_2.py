def check_safety(numbers: list[int]):
    increasing = True
    decreasing = True

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if not 0 < diff <= 3:
            decreasing = False
            break

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if not -3 <= diff < 0:
            increasing = False
            break

    return increasing or decreasing


def main():
    safe_count = 0
    filename = "aoc-dec2-input.txt"

    with open(filename) as file:
        for line in file:
            numbers = list(map(int, line.split()))
            if check_safety(numbers):
                safe_count += 1
                continue

            # otherwise try again removing one level each time
            for i in range(len(numbers)):
                reduced_line = numbers.copy()
                del reduced_line[i]
                if check_safety(reduced_line):
                    safe_count += 1
                    break

    print(f"Total Number of Safe Reports: {safe_count}")


if __name__ == "__main__":
    main()
