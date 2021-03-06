#!/usr/bin/env python3
#
# Created by: Austin de Mora
# Created on: May 2021
# This program checks if it is a leap year or common year

import math


def main():
    # This function checks if it is a leap year or common year

    # Input

    chosen_year = input("Enter the year you have chosen: ")
    print("")

    # process
    try:
        if (int(chosen_year) % 4) == 0:
            if (int(chosen_year) % 100) == 0:
                if (int(chosen_year) % 400) == 0:
                    print("{} is a leap year".format(chosen_year))
                else:
                    print("{} is a common year".format(chosen_year))
            else:
                print("{} is a leap year".format(chosen_year))
        else:
            print("{} is a common year".format(chosen_year))
    except Exception:
        print("Invalid Input")


if __name__ == "__main__":
    main()
