#Aaron Truong
# Lab 10 CIS 247 C

"""
This module demonstrates the use of the FullName class.
It creates several FullName objects, compares them, and sorts them based on last and first names.
"""

from FullName import FullName

try:

    person1 = FullName("Aaron", "Truong")
    person2 = FullName("Brandon", "Chiem")
    person3 = FullName("Julia", "Kim")
    person4 = FullName("John", "Smith")
    person5 = FullName("Donald", "Biden")

    print("\n1. __str__ method:")
    print(f"Person 1: {person1}")
    print(f"Person 2: {person2}")
    print(f"Person 3: {person3}")
    print(f"Person 4: {person4}")
    print(f"Person 5: {person5}")

    print("\n2. __gt__ method:")
    print(f"{person1} > {person2}? {person1 > person2}")
    print(f"{person2} > {person1}? {person2 > person1}")
    print(f"{person4} > {person5}? {person4 > person5}")
    print(f"{person5} > {person4}? {person5 > person4}")
    print(f"{person1} > {person3}? {person1 > person3}")

    people = [person1, person2, person3, person4, person5]

    people.sort()

    print("\nSorting Names")
    for i, person in enumerate(people, 1):
        print(f"  {i}. {person}")

except Exception as e:
    print(f"An error occurred: {e}")