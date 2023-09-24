"""
A python script that tries to convert user input to integer
also handles edge case if user enters anything other than numbers

@usage python3 int_conversion.py 'f'
"""


def main():
    # welcome message
    print("Welcome to the conversion tool (string to integer)")
    # number variable to store the input
    number = input("Enter a number you would like to convert: ")

    # try and except block
    try:
        int_convert = int(number)  # convert to integer
        print(f"your converted integer number: {int_convert}")
    except ValueError:  # raises error if input is anything other than numbers
        print(f"sorry, this input invalid: {number}")
        print("Expected an integer for instance: 1, 2 etc")


if __name__ == "__main__":
    main()
