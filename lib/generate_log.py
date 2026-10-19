
from datetime import datetime
import os


def generate_log(data):
    # Step 1: Validate that data is a list
    if not isinstance(data, list):
        print("Error: Data must be a list.")
        return

    # Step 2: Generate a filename using today's date
    date = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date}.txt"

    # Step 3: Write each log entry to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Step 4: Print a confirmation message
    print(f"Log written to {filename}")


# Example usage
log_data = [
    "User logged in",
    "User updated profile",
    "Report exported"
]

generate_log(log_data)


    # pass
