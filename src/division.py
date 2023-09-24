"""
This script takes 2 numbers from user gives you result of division
also handles an edge case if user enters 0 as a denominator.

@usage python3 division.py 3, 2
"""


def main():

    # takes numerator and denominator from the user
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # try and except block to handle the case if user enters 0
    try:
        divide = (numerator / denominator)  # do the division
    except ZeroDivisionError:
        print("oops, you have entered denominator as 0, can't divide by 0")
    else:
        print(f"Your final division is: {divide}")  # print the final division  # noqa


if __name__ == "__main__":
    main()
