#Aaron Truong
#CIS 247 Lab 2

"""
Args
    Concert Name = String name
    VIP Tickets = Int number of VIP Tickets sold
    General Tickets = Int Number of General Tickets sold

Returns
    Gross Profit = (VIP Ticket * 100) + (General Tickets * 50)
    Venue Profit = Gross Profit * 30%
    Artist Profit = Gross Profit * 70%
"""

def main():
    #varaible declarations
    name = input("Concert Name:")
    vip_tickets = float((input("VIP Tickets:")))
    general_tickets = float(input("General Tickets:"))

    grossProfit = (vip_tickets * 100) + (general_tickets * 50)
    venueProfit = grossProfit * 0.3
    artistProfit = grossProfit * 0.7

    print(f'Venue Profit:{venueProfit: .2f}$')
    print(f'Arist Profit:{artistProfit: .2f}$')
    print(f'Gross Profit:{grossProfit: .2f}$')

main()