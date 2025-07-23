def read_data(file_path):
    """
    Read data from the text file.

    Args:
    - file_path: Path to the text file containing land data.

    Returns:
    - data: A dictionary containing land details.
    """
    data = {}  # Initialize an empty dictionary to store land details
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line of the file into individual pieces of data and assign them to variables
                kitta, city, direction, area, price, status = line.strip().split(', ')
                # Create a dictionary for each land with its details and add it to the data dictionary
                data[kitta] = {
                    'city': city,  # City or district where the land is located
                    'direction': direction,  # Direction the land faces
                    'area': int(area),  # Area of the land in anna
                    'price': int(price),  # Price of the land in Nepalese Rupee
                    'status': status  # Availability status of the land
                }
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        # Create an empty file if not found
        open(file_path, 'w').close()
    return data  # Return the dictionary containing land details
