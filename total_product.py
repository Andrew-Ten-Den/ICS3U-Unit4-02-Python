#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: April 2022
# This program multiplies the product of consecutive integers


def main():
    # this function multiplies the product of consecutive integers

    # this is to keep track of how many times you go through the loop
    loop_counter = 1
    total_product = 1

    # input
    try:
        integer = int(input("Enter a number: "))

        # process & output
        if integer == 0:
            print("\nThe product is 1")
        elif integer == 1:
            print("\nThe product is 1")
        elif integer < 0:
            print("\nUndefined")
        else:
            print("\n", end="")
            while loop_counter <= integer:
                total_product = total_product * loop_counter
                loop_counter = loop_counter + 1
            print("The product is {0}.".format(total_product))
    except Exception:
        print("This was not an integer")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
