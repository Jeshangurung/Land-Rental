from operations import rent_land, return_land, apply_fine, display_menu  # Import functions for land operations
from read import read_data  # Import function to read data from file
from write import write_data  # Import function to write data to file

def main():
    # Load data from file
    file_path = "land_data.txt"
    data = read_data(file_path)  # Read land data from file

    while True:
        # Display menu options and get user choice
        display_menu()  # Display menu options for user interaction
        choice = input("Enter your choice: ")  # Get user choice

        if choice == "1":
            # Rent land
            customer_name = input("Enter customer name: ")  # Prompt user to enter customer name
            rent_land(data, customer_name)  # Call function to rent land
        elif choice == "2":
            # Return land
            kitta = input("Enter kitta number: ")  # Prompt user to enter kitta number
            customer_name = input("Enter customer name: ")  # Prompt user to enter customer name
            duration = int(input("Enter duration of rent (in months): "))  # Prompt user to enter duration
            return_land(data, kitta, customer_name, duration)  # Call function to return land
        elif choice == "3":
            # Apply fine
            kitta = input("Enter kitta number: ")  # Prompt user to enter kitta number
            fine_per_month = float(input("Enter fine amount per month: "))  # Prompt user to enter fine amount
            apply_fine(data, kitta, fine_per_month)  # Call function to apply fine
        elif choice == "4":
            # Exit program
            write_data(file_path, data)  # Write updated data to file
            print("Exiting program.")  # Print exit message
            break  # Exit the loop and program
        else:
            print("Invalid choice. Please choose again.")  # Print message for invalid choice

if __name__ == "__main__":
    main()  # Call main function if the script is executed directly
