#Aaron Truong
#Hw4 CIS 247 C

from Date import Date
from Event import Event

def add_event(events_list):
    print("\n--- Add New Event ---")
    try:
        day = int(input("Enter day (1-31): "))
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year: "))
        start_hour = int(input("Enter start hour (0-23): "))
        end_hour = int(input("Enter end hour (0-23): "))
        event_name = input("Enter event name: ").strip()

        if not (1 <= day <= 31 and 1 <= month <= 12 and year > 0 and 0 <= start_hour < end_hour <= 23 and event_name):
            print("Invalid input. Please check your entries.")
            return

        event_date = Date(day, month, year)
        new_event = Event(event_name, start_hour, end_hour, event_date)

        for existing_event in events_list:
            if new_event.overlaps_with(existing_event):
                print("Error: Event overlaps with existing event:")
                print(f"  {existing_event}")
                return

        events_list.append(new_event)
        print("Event added successfully!")

    except ValueError:
        print("Error: Please enter valid numbers for date and time.")

def cancel_event(events_list):
    print("\n--- Cancel Event ---")
    if not events_list:
        print("No events to cancel.")
        return
    event_name = input("Enter the name of the event to cancel: ").strip()
    for i, event in enumerate(events_list):
        if event.event_name.lower() == event_name.lower():
            events_list.pop(i)
            print(f"Event '{event_name}' has been cancelled.")
            return
    print(f"Event '{event_name}' not found.")

def view_all_events(events_list):
    print("\n--- All Scheduled Events ---")
    if not events_list:
        print("No events scheduled.")
        return
    for i, event in enumerate(events_list, 1):
        print(f"{i}. {event}")

def main():
    print("Convention Center Scheduling System")
    print("=" * 40)
    events_list = []
    while True:
        print("\nMenu Options:")
        print("1. Add an Event")
        print("2. Cancel an Event")
        print("3. View All Events")
        print("4. Quit")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == '1':
            add_event(events_list)
        elif choice == '2':
            cancel_event(events_list)
        elif choice == '3':
            view_all_events(events_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")