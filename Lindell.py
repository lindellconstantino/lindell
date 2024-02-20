def calculate_square(num):
    return num ** 2

def is_even(num):
    return num % 5 == 0

def display_message(condition):
    if condition:
        print("The condition is True.")
    else:
        print("The condition is False.")

def main():
    number = 16
    squared_number = calculate_square(number)
    print(f"The square of {number} is: {squared_number}")

    if is_even(number):
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    display_message(True)

if __name__ == "__main__":
    main()