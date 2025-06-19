#Aaron Truong
#Hw1 CIS 247 C


def ticket_menu():
    print("\n" + "=" * 50)
    print("          MOVIE THEATER SEATING CHART")
    print("=" * 50)
    print("        | Seat Level  | Price per Ticket |")
    print("        |-------------|------------------|")
    print("        | Premium     |      $20.00      |")
    print("        | Standard    |      $12.00      |")
    print("        | Economy     |      $8.00       |")
    print("=" * 50)
    print()

def get_user_input():
    try:
        num_premium = int(input("Enter the number of Premium Tickets you want to purchase: "))
        if num_premium <= 0:
            print("Please enter a positive number.")
        num_standard = int(input("Enter the number of Standard Tickets you want to purchase: "))
        if num_standard <= 0:
            print("Please enter a positive number.")
        num_economy = int(input("Enter the number of Economy Tickets you want to purchase: "))
        if num_economy <= 0:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

    return num_premium, num_standard, num_economy
    
def calculate_total(num_premium, num_standard, num_economy):
    premium_price = 20.00
    standard_price = 12.00
    economy_price = 8.00

    total_premium = num_premium * premium_price
    total_standard = num_standard * standard_price
    total_economy = num_economy * economy_price

    overall_total = total_premium + total_standard + total_economy

    print("\n" + "=" * 50)
    print("          TICKET PURCHASE SUMMARY")
    print("=" * 50)
    print(f"Premium Tickets: {num_premium} x ${premium_price:.2f} = ${total_premium:.2f}")
    print(f"Standard Tickets: {num_standard} x ${standard_price:.2f} = ${total_standard:.2f}")
    print(f"Economy Tickets: {num_economy} x ${economy_price:.2f} = ${total_economy:.2f}")
    print("=" * 50)
    print(f"Overall Total: ${overall_total:.2f}")
    print("=" * 50)
    print("Thank you for your purchase!")


ticket_menu()
calculate_total(*get_user_input())