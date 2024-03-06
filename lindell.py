def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(result)

if __name__ == "__main__":
    main()
