#Aaron Truong
#Lab 10 CIS 247 C

"""
Creating a FullName class that allows comparison based on last name and first name.
"""

class FullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __gt__(self, other):
        if self.last_name > other.last_name:
            return True
        elif self.last_name == other.last_name:
            return self.first_name > other.first_name
        else:
            return False
        