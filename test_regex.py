#!/usr/bin/env python3

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
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")


def phone_numChecker():
    match = re.compile(r"\+([0-9]){3}[\s|-]([0-9]){3}[\s|-]([0-9]){3}[\s|-]([0-9]){2,4}")
    phone_num = input("Enter your phone number (Eg: +250xxx): ")

    if re.fullmatch(match, phone_num):
        print(f"'{phone_num}'looks like a valid phone number")
    else:
        print("Invalid phone number!")


def id_Checker():
    """Validates organizational ID's"""
    match = re.compile(r"(^[^A-Za-z]([0-9]*[a-z]*)*[^0-9]$)")  # Your Regex goes between the double quotes

    org_id = input("Enter your organization's ID: ")

    if re.fullmatch(match, org_id):
        print(f"'{org_id}'looks like a valid ID")
    else:
        print("Invalid ID!")


if __name__ == "__main__":
    # pass
    phone_numChecker()
    id_Checker()
