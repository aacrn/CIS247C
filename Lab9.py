#Aaron Truong
# Lab 9 CIS 247 C

"""
Create a program that asks the user to enter a series of city names and populations. Each name and population should be added to a dictionary as a key/value pair. 
Once they are finished entering these values, use a dictionary comprehension to create a new dictionary featuring only the cities whose populations are over 2 million. 
Print the key/value pairs in the resulting dictionary out.
"""

def main():
    cities = {}
    
    while True:
        city_name = input("Enter a city name (or 'done' to finish): ")
        if city_name.lower() == 'done':
            break
        try:
            population = int(input(f"Enter the population for {city_name}: "))
            cities[city_name] = population
        except ValueError:
            print("Invalid population. Please enter a numeric value.")
    
    # Dictionary comprehension to filter cities with populations over 2 million
    large_cities = {name: pop for name, pop in cities.items() if pop > 2000000}
    
    print("\nCities with populations over 2 million:")
    for name, pop in large_cities.items():
        print(f"{name}: {pop}")

main()