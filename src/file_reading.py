"""
This script attempts to open a user specified file
it also handles the edge case where user wants read a file
that doesn't exists

@usage python3 file_reading.py greet.txt
"""


def main():

    # asks user which file they want to open
    file = str(input("what file would you like to open?: "))

    # try / except block
    try:
        my_file = open(file, "+r")
        print("File content: ")
        print(my_file.read())  # read the file content
        my_file.close()  # close the file
    except FileNotFoundError:
        print("oops, this file doesn't exists")   # file doesn't exist


if __name__ == "__main__":
    main()
