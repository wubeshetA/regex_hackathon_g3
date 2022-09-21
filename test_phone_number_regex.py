#!/usr/bin/env python3

"""A script with regular expressions that can validate a registration form.
   Entries to be validated:
    Phone Number
"""


import re


def emailChecker():
    match = re.compile(r"\+([0-9]){3}[\s|-]?([0-9]){3}[\s|-]?([0-9]){3}[\s|-]?([0-9]){2,4}")  # Your Regex goes between the double quotes

    phone_num = input("Enter your phone number (Eg: +250xxx): ")

    if re.fullmatch(match, phone_num):
        print(f"'{phone_num}'looks like a valid phone number")
    else:
        print("Invalid phone number!")

emailChecker()
