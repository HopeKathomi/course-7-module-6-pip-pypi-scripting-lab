
from datetime import datetime
import os


def generate_log(data):
    # Step 1: Validate the input
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    # Step 2: Generate a filename using today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Step 3: Write each entry to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Step 4: Print a confirmation message
    print(f"Log written to {filename}")

    # Return the filename for the tests
    return filename

if __name__ == "__main__":
    data = ["User logged in", "Report exported"]
    filename = generate_log(data)
    print(f"Log written to {filename}")