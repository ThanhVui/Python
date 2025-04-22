def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num


def main():
    with open("data_1.txt", "r") as file:
        numbers = file.readline().strip().split(",")

    numbers = [int(num) for num in numbers if num.isdigit()]
    perfect_numbers = [num for num in numbers if is_perfect_number(num)]

    occurrences = {}
    for num in perfect_numbers:
        if num not in occurrences:
            occurrences[num] = 1
        else:
            occurrences[num] += 1

    max_frequency = max(occurrences.values())
    most_frequent_numbers = [
        num for num, freq in occurrences.items() if freq == max_frequency
    ]

    print("Perfect numbers from the file:", perfect_numbers)
    print("Occurrences of each perfect number:", end=" ")
    for num, freq in occurrences.items():
        print(f"({num}: {freq})", end=", ")
    print()
    print(
        "Number(s) with the highest frequency:",
        ", ".join(map(str, most_frequent_numbers)),
    )


if __name__ == "__main__":
    main()
