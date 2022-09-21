#!/usr/bin/env python3

"""A script with regular expressions that can validate a registration form.
   Entries to be validated:
    Organization ID
"""


import re


def id_Checker():
    """Validates organizational ID's"""
    match = re.compile(r"(^[^A-Za-z]([0-9]*[a-z]*)*[^0-9]$)")  # Your Regex goes between the double quotes

    org_id = input("Enter your organization's ID: ")

    if re.fullmatch(match, org_id):
        print(f"'{org_id}'looks like a valid ID")
    else:
        print("Invalid ID!")

id_Checker()
