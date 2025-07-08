#Aaron Truong
#Date Hw4 CIS 247 C

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"

    def __eq__(self, other):
        return isinstance(other, Date) and (self.day, self.month, self.year) == (other.day, other.month, other.year)