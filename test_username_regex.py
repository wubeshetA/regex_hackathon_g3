#!/usr/bin/env python3

"""A script with regular expressions that can validate a registration form.
   Entries to be validated:
    username
"""

import re

def user_name_checker():
    """ Check if username is valid """
    match = re.compile(r"[A-Z]{1}[a-z]+\S[A-Z]{1}[a-z]+")  # Your Regex goes between the double quotes
    username = input("Enter the Username: ")

    if re.fullmatch(match, username):
        print(f"'{username}'looks like a valid Email")
    else:
        print("Invalid Username")
