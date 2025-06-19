#Aaron Truong
#Hw2 CIS 247 C


def calculate_hot_dogs_needed(attendees, dogs_per_person): #Calculate the number of hot dog packages and leftovers
    total_dogs = attendees * dogs_per_person
    packages_needed = total_dogs // 10
    leftovers = total_dogs % 10
    return packages_needed, leftovers

def calculate_hot_dog_buns_needed(attendees, dogs_per_person): #Calculate the number of hot dog bun packages and leftovers
    total_buns = attendees * dogs_per_person
    packages_needed = total_buns // 8
    leftovers = total_buns % 8
    return packages_needed, leftovers

def main():
    try: #Get user input and validate
        attendees = int(input("Enter the number of people attending the cookout: "))
        dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))
        if attendees < 0 or dogs_per_person < 0:
            raise ValueError("Please enter non-negative integers.")
    except ValueError as e:
        print(e)
        return

    hot_dog_packages, hot_dog_leftovers = calculate_hot_dogs_needed(attendees, dogs_per_person)
    bun_packages, bun_leftovers = calculate_hot_dog_buns_needed(attendees, dogs_per_person)

    #Print results
    print(f"\nMinimum number of packages of hot dogs required: {hot_dog_packages}")
    print(f"Minimum number of packages of hot dog buns required: {bun_packages}")
    print(f"Number of hot dogs that will be left over: {hot_dog_leftovers}")
    print(f"Number of hot dog buns that will be left over: {bun_leftovers}")

main()