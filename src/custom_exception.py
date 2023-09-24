from negative_value import NegativeValueError


def number_check(number):
    """Method to check if user entered negative number"""

    if number < 0:
        raise (NegativeValueError)


def main():
    """main method"""

    # try and except block to take user input and check it
    try:
        num = int(input("Enter a number: "))
        number_check(num)
        print(f"your positive number is: {num}")  # print number
    except NegativeValueError:
        print("sorry, the number is negative")  # error rasied


if __name__ == "__main__":
    main()
