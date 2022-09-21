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
    match = re.compile(r"[a-z]\.[a-z]+@[a-z]+\.(email)")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def password_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def DOB_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


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
    pass
