# Program to check if a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")
