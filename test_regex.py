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
    """ Check if full name is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    name = input("Enter the Full Name: ")

    if re.fullmatch(match, name):
        print(f"'{name}'looks like a valid Name")
    else:
        print("Invalid Full name")


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
    match = re.compile(r"")  # Your Regex goes between the double quotes
    password = input("Enter the Password: ")

    if re.fullmatch(match, password):
        print(f"'{password}'looks like a valid Password")
    else:
        print("Invalid Password")


def DOB_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    dob = input("Enter the DOB: ")

    if re.fullmatch(match, dob):
        print(f"'{dob}'looks like a valid DOB")
    else:
        print("Invalid DOB")


def phone_number_checker():
    """ Check if email is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    phone = input("Enter the Phone number: ")

    if re.fullmatch(match, phone):
        print(f"'{phone}'looks like a valid Phone Number")
    else:
        print("Invalid Phone Number")


def id_checker():
    """ Check if Id is valid """
    match = re.compile(r"")  # Your Regex goes between the double quotes
    id = input("Enter the Id: ")

    if re.fullmatch(match, id):
        print(f"'{id}'looks like a valid Id")
    else:
        print("Invalid Id")


if __name__ == "__main__":
    pass
