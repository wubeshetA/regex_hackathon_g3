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
    match = re.compile(r"[A-Za-z]+\s[A-Za-z]+\.?\/?\s[A-Za-z]+")  # Your Regex goes between the double quotes
    full_name = input("Enter the full name: ")

    if re.fullmatch(match, full_name):
        print(f"'{full_name}'looks like a valid full name")
    else:
        print("Invalid full name")


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
    # pass
    full_name_checker()
    password_checker()

