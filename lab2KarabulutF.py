# lab2KarabulutF.py
# Furkan Karabulut (fkarabu)
# Class: CSC 205-002
# Date: 1/25/2024

from datetime import datetime

# Give the user specific instructions regarding the type and range of values they should enter. If they input a year
# before the Gregorian calendar was adopted, output an error message. Your output should include the year
# with a message that uses the appropriate verb tense (is/was/will be).
# If the user enters a year that is a leap year, output a message indicating that the year is/was/will be a leap
# year. Otherwise, output a message indicating that the year is/was/will be a common year.
def main():
    # print the header
    print('-----------------------------------------------------------------------------------------------')
    print('This program will determine if a year is a leap year or not.')
    print('A year is a leap year if it is divisible by 4, unless it is also divisible by 100 but not 400.')
    print('The year 1582 was the first year of the Gregorian calendar.')
    print('-----------------------------------------------------------------------------------------------')

    # get the input from the user and get the current year
    current_year = datetime.now().year
    input_year = int(input('Please enter a year: '))
    print('-----------------------------------------------------------------------------------------------')

    # print the output
    print('Input:               Output:')
    print(f"{input_year:<21}{calculate_leap_year(input_year, current_year)}")


# calculate the leap year with a function
# input: year, current_time_year
# output: a string with the year and the verb tense
def calculate_leap_year(year, current_time_year):
    # check if the year is before the Gregorian calendar was adopted
    if year < 1582:
        return f"Error! {year} was before adoption of the Gregorian calendar"
    # first calculate the verb tense
    elif year == current_time_year:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return f"{year} is a leap year"
        else:
            return f"{year} is not a leap year"
    elif year > current_time_year:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return f"{year} will be a leap year"
        else:
            return f"{year} will not be a leap year"
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return f"{year} was a leap year"
        else:
            return f"{year} was not a leap year"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
