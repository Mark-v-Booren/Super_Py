
import argparse
import csv
from datetime import date, timedelta
import os
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt
import pandas as pd

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass


# Add the command-line argument for advancing the time
def save_date_to_file(filename, date_value):
    with open(filename, 'w') as file:
        file.write(str(date_value))


current_date = date.today()


def get_script_directory():
    script_path = os.path.abspath('date_now.txt')
    script_directory = os.path.dirname(script_path)
    return script_directory


directory = get_script_directory()
print(f'Script directory: {directory}')


# create ïn_stock.CSV-file
def create_csv(in_stock):
    if os.path.isfile(in_stock):
        print(f"File '{in_stock}' found.")
        return

    rows = []
    # Open the CSV file in write mode
    with open(in_stock, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['id', 'name', 'price', 'exp-date', 'date'])
        # Write the data rows
        writer.writerows(rows)
        print(f"File '{in_stock}' created.")
        return


create_csv('in_stock.csv')


# create sold.CSV-file
def create_csv(sold):
    if os.path.isfile(sold):
        print(f"File '{sold}' found.")
        return
    # test data for the rows
    rows = []
    # Open the CSV file in write mode
    with open(sold, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'price', 'exp-date', 'date'])
        writer.writerows(rows)
        print(f"File '{sold}' created.")
        return


create_csv('sold.csv')


# add report data
def display_csv_in_stock(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    print("************* In stock: ***************: ")
    # Create a table
    table = Table(show_header=True, header_style="green")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Amount")
    table.add_column("Price")
    table.add_column("Expire Date")
    table.add_column("Entry Date")
    # Add rows to the table
    for row in rows:
        table.add_row(*row)
    # Create a console and print the table
    console = Console()
    console.print(table)


def display_csv_sold(filename):
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    print("************* Sold: ***************: ")
    # Create a table
    table = Table(show_header=True, header_style="green")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Price")
    table.add_column("Date")
    for row in rows:
        table.add_row(*row)
    console = Console()
    console.print(table)


def add_product_to_csv_in_stock(filename,
                                name,
                                price,
                                expire_date,
                                ):
    # Open the CSV file in append mode
    date = current_date
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the new product row
        writer.writerow([get_last_id(filename) + 1, name,
                         price,
                         expire_date,
                         date])
    print(f"Product '{name}' added to '{filename}' successfully.")


# function to sell a product : check if in istocjk and make profit balance
def add_product_to_csv_sold(file, name):
    with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        product = None
        for row in reader:
            if row['name'] == name:
                product = row
                # print(f"Product {name} found in stock! ")
                break
    if product is None:
        print(f"Product {name} not found in stock...")
        return
    with open('sold.csv', 'a', newline='') as csv_file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(product)

    print(f"Product with ID {name} parsed and appended to sold.csv")


def remove_when_sold(csv_file, name):
    # Read the contents of the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    # Find the row(s) with the specified name
    matching_rows = [row for row in rows if row['name'] == name]

    if not matching_rows:
        print(f"No rows found with the name '{name}'")
        return
    # Remove the matching rows from the list of rows
    for row in matching_rows:
        rows.remove(row)
    # Overwrite the CSV file with the updated contents
    with open(csv_file, 'w', newline='') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Row(s) with the name '{name}' removed from {csv_file}")


def get_last_id(filename):
    # Open the CSV file in read mode
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        # Find the last ID in the existing data
        if len(rows) > 1:
            last_row = rows[-1]
            last_id = int(last_row[0])
        else:
            last_id = 0
    return last_id


def calculate_profit(csv_file):
    # Read the contents of the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        total_profit = 0
        for row in reader:
            try:
                price = float(row['price'])
                total_profit += price
            except ValueError:
                print(f"Invalid price value found in row: {row}")

    print(f'The total profit of today is {total_profit}!')


def check_expired_products(file):

    # # Read the contents of the CSV file
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        # field_names = reader.fieldnames
        products = list(reader)
    # # Get the current date or a date in the future
    date_now = input("Enter the current date (YYYY-MM-DD): ")

    expired_products = []
    for product in products:
        expire_date_str = product['exp-date']
        if expire_date_str < date_now:
            expired_products.append(product)
            print(f'product {expired_products} == expired! ')
        else:
            print('all good!')


parser = argparse.ArgumentParser(description='Manage products in the in_stock.csv file')
# Create subparser for adding to in stock csv
subparsers = parser.add_subparsers(dest='command', help='Available commands')
add_parser = subparsers.add_parser('add', help='Add a product to the in_stock.csv file')
add_parser.add_argument('--name', type=str, help='Product name', required=True)
add_parser.add_argument('--price', type=float,
                        help='Price of product', required=True)
add_parser.add_argument('--expire_date', type=str,
                        help='Expiration date (YYYY-MM-DD)', required=True)

# Create subparser for adding to sold csv
sell_parser = subparsers.add_parser('sold', help=' Add a product to the sold.csv file')
sell_parser.add_argument('--name', help=' Add a product to the sold.csv file')
sell_parser.add_argument('--price', help=' Add a product to the sold.csv file')

#  Create report parser
parser.add_argument('--report', help='Command to execute')

parser.add_argument('--expired', help='Path to the CSV file')

# advance-time parser by a number of days
parser.add_argument('--advance-time', type=int,
                    help='Advance time by specified number of days')

# Parse the arguments from the command line
args = parser.parse_args()

if args.expired == 'check':
    check_expired_products('in_stock.csv')

if args.command == 'add':
    add_product_to_csv_in_stock('in_stock.csv', args.name, args.price, args.expire_date)

if args.command == 'sold':
    add_product_to_csv_sold('in_stock.csv', args.name)
    remove_when_sold('in_stock.csv', args.name)

if args.advance_time:
    future_date = current_date + timedelta(days=args.advance_time)
    current_date = future_date

if args.report == 'sold':
    display_csv_sold('sold.csv')
    df = pd.read_csv('sold.csv')
    x = df['id']
    y = df['price']
# Plot the data
    plt.plot(x, y)
    plt.xlabel('id-s')
    plt.ylabel('prices')
    plt.title('In da house')
    plt.grid(True)
    plt.show()

if args.report == 'in_stock':
    display_csv_in_stock('in_stock.csv')
    df = pd.read_csv('in_stock.csv')
    x = df['id']
    y = df['price']
# Plot the data
    plt.plot(x, y)
    plt.xlabel('id-s')
    plt.ylabel('prices')
    plt.title('In da house')
    plt.grid(True)
    plt.show()

if args.report == 'total':
    display_csv_in_stock('in_stock.csv')
    display_csv_sold('sold.csv')

if args.report == 'profit':
    calculate_profit('sold.csv')
    df = pd.read_csv('sold.csv')
    x = df['id']
    y = df['price']
# Plot the data
    plt.plot(x, y)
    plt.xlabel('date')
    plt.ylabel('prices')
    plt.title('Profit')
    plt.grid(True)
    plt.show()

print("""
                                  ---Welcome by SUPERPY
     _____  __  __  _____  _____  _____  _____  __  __
    /	 /|/ /|/ /|/    /|/    /|/    /|/    /|/ /|/ /|
   /  __/ / / / / /  / / /  __/ /  / / /  / / / / / / |
  /__  /|/ / / / /  / / /  __/|/  / / /  / / / /_/ / /
 /    / / /_/ / / ___/ /    /|/   _/ / ___/ /__   / /
/____/ /_____/ /_/|  |/____/ /_/|_| /_/|  | | /_ / /
|    | |     | | ||__||    | | || | | ||__|/|_| | /
|____|/|_____|/|_|/   |____|/|_||_|/|_|/      |_|/

Mark van Booren 2023---
""")

print(f"Today's date: {current_date}")


if __name__ == "__main__":
    main()
