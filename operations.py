from datetime import datetime

def rent_land(data, customer_name):
    """
    Rent land to a customer.

    Args:
    - data: A dictionary containing land details.
    - customer_name: Name of the customer.
    """
    rented_lands = []  # List to store rented lands

    while True:
        available_lands = [k for k, v in data.items() if v['status'] == 'Available']  # List of available lands
        if not available_lands:
            print("No lands available for rent.")
            break

        print("Available Lands:")
        for k in available_lands:
            print(f"Kitta Number: {k}, City: {data[k]['city']}, Direction: {data[k]['direction']}, Area: {data[k]['area']} anna")

        kitta = input("Enter the kitta number you want to rent (or 'done' to finish): ")
        if kitta.lower() == 'done':
            break

        if kitta in available_lands:
            data[kitta]['status'] = 'Not Available'  # Mark the land as rented
            duration = int(input("Enter duration of rent (in months): "))
            total_price = data[kitta]['price'] * duration
            rented_land = {
                'kitta': kitta,
                'city': data[kitta]['city'],
                'direction': data[kitta]['direction'],
                'area': data[kitta]['area'],
                'customer_name': customer_name,
                'duration': duration,
                'total_price': total_price
            }
            rented_lands.append(rented_land)  # Add rented land to the list
            print(f"Land {kitta} has been rented to {customer_name}.")

    if rented_lands:
        # Generate invoice if lands are rented
        invoice = f"Invoice_{customer_name}.txt"
        with open(invoice, 'a') as file:  # Append mode to add more rented lands to the same invoice
            file.write("\nRented Lands:\n")
            file.write("-------------\n")
            file.write(f"Customer Name: {customer_name}\n")
            for rented_land in rented_lands:
                file.write(f"Kitta Number: {rented_land['kitta']}\n")
                file.write(f"City/District: {rented_land['city']}\n")
                file.write(f"Land Faced: {rented_land['direction']}\n")
                file.write(f"Area of Land: {rented_land['area']} anna\n")
                file.write(f"Duration of Rent: {rented_land['duration']} months\n")
                file.write(f"Total Amount: NPR {rented_land['total_price']}\n")

def return_land(data, kitta, customer_name, duration):
    """
    Return rented land.

    Args:
    - data: A dictionary containing land details.
    - kitta: The kitta number of the land to return.
    - customer_name: Name of the customer.
    - duration: Duration of rent in months.
    """
    if kitta in data and data[kitta]['status'] == 'Not Available':
        data[kitta]['status'] = 'Available'
        total_price = data[kitta]['price'] * duration
        vat = total_price * 0.13
        final_price = total_price + vat
        # Generate invoice
        invoice = f"Invoice_{kitta}_{customer_name}_{duration}months.txt"
        with open(invoice, 'w') as file:
            file.write(f"Customer Name: {customer_name}\n")
            file.write(f"Kitta Number: {kitta}\n")
            file.write(f"City/District: {data[kitta]['city']}\n")
            file.write(f"Land Faced: {data[kitta]['direction']}\n")
            file.write(f"Date and Time of Returning: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Duration of Rent: {duration} months\n")
            file.write(f"Area of Land: {data[kitta]['area']} anna\n")
            file.write(f"Total Amount: NPR {total_price}\n")
            file.write(f"Vat: NPR {vat}\n")
            file.write(f"Final Amount: NPR {final_price}\n")
            
        print(f"Land {kitta} has been returned by {customer_name}. Invoice generated: {invoice}")
    else:
        print("Invalid kitta number or land is not rented.")

def apply_fine(data, kitta, fine_per_month):
    """
    Apply fine for late return of land.

    Args:
    - data: A dictionary containing land details.
    - kitta: The kitta number of the land.
    - fine_per_month: Fine amount per month.
    """
    if kitta in data and data[kitta]['status'] == 'Not Available':
        # Calculate late months
        late_months = 3  # For demonstration purpose, assuming 3 months late
        fine_amount = int(fine_per_month * late_months)
        print(f"Fine applied: NPR {fine_amount}")
    else:
        print("Invalid kitta number or land is not rented.")

def display_menu():
    """Display menu options to the user."""
    print("\t\t\t |---------------------|")
    print("\t\t\t | TechnoPropertyNepal |")
    print("\t\t\t |---------------------|")
    print("\nMenu Options:")
    print("1. Rent Land")
    print("2. Return Land")
    print("3. Apply Fine")
    print("4. Exit")
