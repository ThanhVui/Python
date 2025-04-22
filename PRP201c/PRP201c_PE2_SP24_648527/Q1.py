import random


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_valid_range(lower_prompt, upper_prompt):
    while True:
        try:
            lower_bound = float(input(lower_prompt))
            upper_bound = float(input(upper_prompt))
            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                print(
                    "Invalid range. The lower bound must be less than the upper bound."
                )
        except ValueError:
            print("Invalid input. Please enter floating-point numbers.")


def generate_random_floats(num_floats, lower_bound, upper_bound):
    return [
        round(random.uniform(lower_bound, upper_bound), 2) for _ in range(num_floats)
    ]


def main():
    num_floats = get_positive_integer(
        "How many random floating-point numbers would you like to generate? "
    )
    lower_bound, upper_bound = get_valid_range(
        "Enter the lower bound of the range: ", "Enter the upper bound of the range: "
    )
    random_list = generate_random_floats(num_floats, lower_bound, upper_bound)

    print("Generated list of floating-point numbers:", random_list)
    average = sum(random_list) / len(random_list)
    minimum = min(random_list)
    print("Average of the numbers:", average)
    print("Minimum value in the list:", minimum)


if __name__ == "__main__":
    main()
