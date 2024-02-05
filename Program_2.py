def inches_to_centimeters():
    while True:
        # enter a value in inches
        inches = float(input("Enter a length in inches (or a negative value to quit): "))

        # Check if the user wants to quit
        if inches < 0:
            print("Program ends")
            break

        # Convert inches to centimeters and display the result
        centimeters = inches * 2.54
        print(f"{inches} inches is equal to {centimeters} centimeters.")


if __name__ == "__main__":
    inches_to_centimeters()