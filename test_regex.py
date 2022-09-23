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
    """ Check if username is valid """
    match = re.compile(r"[A-Z]{1}[a-z]+\S[A-Z]{1}[a-z]+")  # Your Regex goes between the double quotes
    username = input("Enter the Username: ")

    if re.fullmatch(match, username):
        print(f"'{username}'looks like a valid Username")
    else:
        print("Invalid Username")


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
    password_checker()