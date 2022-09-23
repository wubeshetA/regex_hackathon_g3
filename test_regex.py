#!/usr/bin/env python

"""A script with regular expressions that can validate a registration form.
   Entries to be validated:
    Full Name
    User Name
    Email
    Password
    Date of Birth
    Phone Number
    Organization ID
"""


import re


def full_name_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def user_name_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def email_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def password_checker():
    """ Check if password is valid """
    match = re.compile(r"^(?=(?:.*[a-z]){2})(?=(?:.*[A-Z]){2})(?=(?:.*\d){2})(?=(?:.*[!@#$%^&*-]){2}).{8}$")  # Your Regex goes between the double quotes
    email = input("Enter the Password: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Password")
    else:
        print("Invalid Password")


def DOB_checker():
    """ Check if date of birth is valid """
    match = re.compile(r"/^(0?[1-9]|[12][0-9]|3[01])[\/._-](0?[1-9]|1[012])[\/._-]\d{4}$/")  # Your Regex goes between the double quotes
    DOB = input("Enter the date of birth: ")

    if re.fullmatch(match, DOB):
        print(f"'{DOB}'looks like a valid date of birth")
    else:
        print("Invalid date of birth")


def phone_number_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def id_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


if __name__ == "__main__":
    # pass
    password_checker()
    DOB_checker()
