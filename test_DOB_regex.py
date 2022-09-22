#!/usr/bin/env python

"""A script with regular expressions that can validate a registration form.
   Entries to be validated:
    Date of birthday
"""


import re

def DOB_checker():
    """ Check if email is valid """
    match = re.compile(r"/^(0?[1-9]|[12][0-9]|3[01])[/._-](0?[1-9]|1[012])[/._-]\d{4}$/")  # Your Regex goes between the double quotes
    DOB = input("Enter the date of birth: ")

    if re.fullmatch(match, DOB):
        print(f"'{DOB}'looks like a valid date of birth")
    else:
        print("Invalid date of birth")
