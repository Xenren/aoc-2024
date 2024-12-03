import re


def main():
    filename = "aoc-dec3-input.txt"

    regex = r"mul\(\d{1,3},\d{1,3}\)"
    total = 0
    with open(filename) as file:
        for line in file:
            matches = re.findall(regex, line)
            # print(matches)
            for m in matches:
                # print(m)
                nums = m.split(",")
                # print(nums)
                num1 = nums[0].lstrip("mul(")
                num2 = nums[1].rstrip(")")
                # print(f"num1:{num1}; num2: {num2}")
                total += int(num1) * int(num2)
    print(f"Result of Multiplications: {total}")


if __name__ == "__main__":
    main()
