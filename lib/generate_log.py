from datetime import datetime


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    data = ["User logged in", "Report exported"]
    generate_log(data)