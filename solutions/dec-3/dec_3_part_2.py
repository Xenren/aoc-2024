import re


def main():
    filename = "aoc-dec3-input.txt"

    mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"

    # thought I needed these
    # do_regex = r"do\(\)"
    # dont_do_regex = r"don't\(\).*?do\(\)"
    # dont_regex = r"don't\(\).*"

    total = 0

    flag = True
    # easier to read entire file for this problem
    content = open(filename).read().strip()

    for i in range(len(content)):

        # look for first do/dont
        if content[i:].startswith("do()"):
            flag = True
        if content[i:].startswith("don't()"):
            flag = False

        # then look for mul matches like normal
        mul = re.match(mul_regex, content[i:])

        # only add product to total if match found and flag is currently active (True)
        if mul and flag:
            num1 = int(mul.group(1))
            num2 = int(mul.group(2))
            total += num1 * num2

    print(f"Result of Multiplications: {total}")


if __name__ == "__main__":
    main()
