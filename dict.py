"""
1. Real-World Python Dictionary Applications
Task 1: Restaurant Menu Update
You are given an initial structure of a restaurant menu stored in a nested dictionary. 
Your task is to update this menu based on given instructions. 
This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

Problem Statement:
Given the initial menu:
"""
restaurant_menu = {
    "Starters": {"Soup ": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.
restaurant_menu["Beverages"] = {"Coffee": 2.50, "Tea  ": 1.99}

# Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters".
del restaurant_menu["Starters"]["Bruschetta"]

for k, v in restaurant_menu.items():
    print("\n",k, "options:")
    for food, price in v.items():
        print(f" - {food}\t{price:.2f}")
print()

"""
2. Advanced Data Handling with Python
Task 1: Hotel Room Booking Tracker
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Problem Statement:
Develop a program that manages room bookings, where each room has details such as booking status (booked/available) 
and customer name.
Implement functions to:
 - Book a room (mark as booked and assign to a customer).
 - Check-out a customer (mark room as available and remove customer name).
 - Display the status of all rooms.
 - Start with this initial hotel room structure:
"""
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(hotel_rooms, room_nbr, customer_name):
    print(f"\nTrying to book room {room_nbr} for {customer_name}. Result: ")
    if room_nbr not in hotel_rooms:
        print(" No such room number")
    elif hotel_rooms[room_nbr]["status"] == "booked":
        print(" Room already booked")
    else:
        hotel_rooms[room_nbr]["status"] = "booked"
        hotel_rooms[room_nbr]["customer"] = customer_name
        print(f" Room {room_nbr} booked for {customer_name}")

def check_out(hotel_rooms, room_nbr):
    print(f"\nTrying to check out customer from room {room_nbr}. Result: ")
    if room_nbr not in hotel_rooms:
        print(" No such room number")
    elif hotel_rooms[room_nbr]["status"] == "available":
        print(" Room already available")
    else:
        hotel_rooms[room_nbr]["status"] = "available"
        hotel_rooms[room_nbr]["customer"] = ""
        print(f" Customer checked out from room {room_nbr}")

def display_room_status(hotel_rooms):
    print("\nRoom Status:")
    for room_nbr, room_info in hotel_rooms.items():
        status = room_info["status"]
        customer = room_info["customer"] if room_info["customer"] else "None"
        print(f" Room {room_nbr}: {status} \t Customer: {customer}")

book_room(hotel_rooms, "100", "Al")
book_room(hotel_rooms, "101", "Peggy")
book_room(hotel_rooms, "102", "Bud")

display_room_status(hotel_rooms)

check_out(hotel_rooms, "100")
check_out(hotel_rooms, "101")
check_out(hotel_rooms, "101")

display_room_status(hotel_rooms)

print()
"""
Task 2: E-commerce Product Search Feature
Put your data handling and string manipulation skills to the test by creating a product search feature 
for an e-commerce platform.

Problem Statement:
Create a system that holds a dictionary of products where each product has attributes like name, category, and price.
Implement a search function that allows searching for products by name, 
returning a list of matching products (case-insensitive search).
Handle cases where no matches are found.
Example product dictionary:
"""
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
def search_products_by_name(products, search_name):
    matches = []
    for id, product in products.items():
        if search_name.lower() in product["name"].lower():
            matches.append(product)
    return matches if matches else None

for item in ['shirt', 'phone', 'pants', 'laptop']: # checking these four items
    print(f"Is {item} in products? ", 'Yes' if search_products_by_name(products, item) else 'No')
print()
"""
3. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement:
Develop a program that tracks customer service tickets, each with a unique ID, customer name, issue description,
and status (open/closed).
Implement functions to:
 - Open a new service ticket.
 - Update the status of an existing ticket.
 - Display all tickets or filter by status.
 - Initialize with some sample tickets and include functionality for additional ticket entry.

Example ticket structure:
"""
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
ticket_counter = 3

while True:
    print("\nCustomer Service Ticket Tracker")
    print("1. Open a New Ticket")
    print("2. Update Ticket Status")
    print("3. Display Tickets")
    print("4. Exit\n")

    choice = input("Enter your choice (between 1 and 4): ")

    if choice == '1': # New Ticket
        customer = input("Enter Customer Name: ")
        issue_descr = input("Enter Issue Description: ")
        ticket_id = f"Ticket{ticket_counter:03d}"
        service_tickets[ticket_id] = {
            "Customer": customer,
            "Issue": issue_descr,
            "Status": "open"
        }
        print(f"Ticket{ticket_counter:03d} Created Successfully!")
        ticket_counter += 1
    elif choice == '2': # Update Ticket
        ticket_id = input("Enter Ticket ID: ")
        if ticket_id not in service_tickets:
            print(f"Ticket ID {ticket_id} Not Found.")
        else:
            service_tickets[ticket_id]["Status"] = input("Enter Status (open/closed): ")
    elif choice == '3': # Print all tickets
        if not service_tickets:
            print("There are currently no tickets.")
        else:
            for ticket_id, ticket_data in service_tickets.items():
                print(f"\nTicket ID:   {ticket_id}")
                print(f"Customer:    {ticket_data['Customer']}")
                print(f"Issue:       {ticket_data['Issue']}")
                print(f"Status:      {ticket_data['Status']}")
    elif choice == '4':
        print("\nGoodbye!\n")
        break
    else:
        print("Invalid choice. Please try again.")


"""
4. Python Essentials for Business Analytics
Task 1: Sales Data Cloning and Modification
Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

Problem Statement:
You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy
of this data and update the sales figures for a specific week.

Given Sales Data:
"""
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
"""
Create a deep copy of weekly_sales.
Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.
"""
import copy
deepcopy_weekly_sales = copy.deepcopy(weekly_sales)
deepcopy_weekly_sales["Week 2"]["Electronics"] = 18000

print("Original Week 2:", weekly_sales["Week 2"], "\n")
print("Deepcopy Week 2:", deepcopy_weekly_sales["Week 2"], "\n")