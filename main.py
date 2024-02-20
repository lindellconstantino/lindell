def greet_user(zodiac):
    return f"Gar, {zodiac}!"

def calculate_square(num):
    return num ** 2

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    user_name = input("Enter your zodiac: ")
    print(greet_user(user_name))

    number = int(input("Enter a number to calculate its square: "))
    print(f"The square of {number} is: {calculate_square(number)}")

    check_prime = int(input("Enter a number to check if it's prime: "))
    if is_prime(check_prime):
        print(f"{check_prime} is a prime number.")
    else:
        print(f"{check_prime} is not a prime number.") 