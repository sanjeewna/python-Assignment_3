def get_numbers():
    numbers = []

    while True:
        num_input = input("Enter a number (or press Enter to quit): ")

        if num_input == '':
            break

        try:
            number = float(num_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return numbers


if __name__ == "__main__":
    numbers = get_numbers()

    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"The smallest number is: {smallest}")
        print(f"The largest number is: {largest}")
    else:
        print("No numbers were entered.")