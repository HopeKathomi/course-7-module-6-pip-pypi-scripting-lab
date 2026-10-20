
from datetime import datetime


def generate_log(data):
    # Validate the input
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # Generate today's date in YYYYMMDD format
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Write each entry to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    return filename

if __name__ == "__main__":
    data = ["User logged in", "Report exported"]
    generate_log(data)