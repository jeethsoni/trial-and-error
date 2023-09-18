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
        print(divide)  # print the final division


if __name__ == "__main__":
    main()
