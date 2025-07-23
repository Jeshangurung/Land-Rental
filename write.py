def write_data(file_path, data):
    """
    Write data to the text file.

    Args:
    - file_path: Path to the text file to write data.
    - data: A dictionary containing land details.
    """
    try:
        with open(file_path, 'w') as file:
            for kitta, details in data.items():
                # Write each land's details to the file in a specific format
                file.write(f"{kitta}, {details['city']}, {details['direction']}, {details['area']}, {details['price']}, {details['status']}\n")
    except Exception as e:
        # Handle any exceptions that occur during file writing
        print(f"Error writing data to file: {e}")
