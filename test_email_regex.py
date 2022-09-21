#!/usr/bin/env python3

"""A script with regular expressions that can validate a registration form.
   Entries to be validated:
    email
"""

import re

def full_name_checker():
    """ Check if email is valid """
    match = re.compile(r"[a-z]\.[a-z]+@[a-z]+\.(email)")  # Your Regex goes between the double quotes
    email = input("Enter the Email: ")

    if re.fullmatch(match, email):
        print(f"'{email}'looks like a valid Email")
    else:
        print("Invalid Email")

