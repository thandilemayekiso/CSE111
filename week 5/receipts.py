import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read a CSV into a dictionary using the specified column as the key."""
    dictionary = {}
    try:
        with open(filename, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) > 0:
                    key = row[key_column_index]
                    dictionary[key] = row
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        raise
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
        raise
    return dictionary

def main():
    PRODUCTS_FILE = "products.csv"
    REQUEST_FILE = "request.csv"
    SALES_TAX_RATE = 0.06

    try:
        products_dict = read_dictionary(PRODUCTS_FILE, 0)

        print("Inkom Emporium")
        print()

        total_items = 0
        subtotal = 0.0

        with open(REQUEST_FILE, mode='r', newline='') as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header
            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                try:
                    product = products_dict[product_id]
                    name = product[1]
                    price = float(product[2])
                    line_total = quantity * price

                    print(f"{name}: {quantity} @ {price:.2f}")

                    total_items += quantity
                    subtotal += line_total

                except KeyError:
                    print("Error: unknown product ID in the request.csv file")
                    print(f"'{product_id}'")
                    raise

        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print()

        # Print current date and time
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

    except FileNotFoundError as e:
        print(f"Error: file not found\n{e}")
       

if __name__ == "__main__":
    main()
    
