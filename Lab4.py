#Aaron Truong
#Lab 4 CIS 247 C


def main():
    sales = []
    num_stores = int(input("Enter the number of stores: "))
    
    for i in range(num_stores):
        sale = int(input(f"Enter today’s sales for store {i + 1}: "))
        sales.append(sale)
    
    print("\nSALES BAR CHART  (Each * = $100)\n")
    
    for i in range(num_stores):
        num_asterisks = sales[i] // 100
        print(f"Store {i + 1}: {'*' * num_asterisks}")

main()