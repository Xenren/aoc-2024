def count_safe_results(filename: str):
    safe_count = 0

    with open(filename) as file:
        for line in file:
            direction = None
            numbers = line.split()
            for i in range(1, len(numbers)):
                diff = int(numbers[i]) - int(numbers[i - 1])

                if diff == 0 or abs(diff) > 3:
                    direction = "unsafe"
                    break

                if diff > 0 and direction != "dec":
                    direction = "inc"
                elif diff < 0 and direction != "inc":
                    direction = "dec"
                else:
                    direction = "unsafe"
                    break

            if direction != "unsafe":
                print(numbers)
                safe_count += 1

    return safe_count


def main():
    filename = "aoc-dec2-input.txt"
    safe_reports = count_safe_results(filename)
    print(f"Total Number of Safe Reports: {safe_reports}")


if __name__ == "__main__":
    main()
