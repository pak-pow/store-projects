import csv
import time
import os
import datetime

FILENAME = "bale.csv"
headers = ["Name", "Item", "Price", "How Many?", "Total", "Time"]

def create_file():

    with open(FILENAME, "w", newline = "") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

def add_record():
    with open(FILENAME, "a", newline = "") as csv_file:

        print ("------" * 6)
        name = input("Enter name: ").title().strip()
        item = input("Enter item: ").title().strip()

        try:
            price = float(input("Enter Price: ").strip())
        except ValueError:
            print("Please input a number")

        how_many = int(input("Enter How many item: "))
        total = int(price) * int(how_many)

        writer = csv.writer(csv_file)
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([name, item, price, how_many, total, now_str])
        print ("Input has been recorded!")
        print ("------" * 6)


def read_record():
    with open(FILENAME, "r", newline = "") as csv_file:
        reader = csv.DictReader(csv_file)
        records = list(reader)

        if records:
            print("------"*6)
            print ("Listing all records...")
            print ("======" * 6, "\n")
            print("Name | Item = Price x Many = Total | Timestamp")
            print ("______" * 6)
            for line in records:
                print (f"{line["Name"]} | {line["Item"]} = {line["Price"]} x {line["How Many?"]} = {line["Total"]} | TimeStamp: {line["Time"]}")
            print ("")
            print ("======" * 6, "\n")
        else:
            print("There is no record")

def delete_record():
    name_to_delete = input("Enter name to delete: ").strip()

    with open(FILENAME, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        records = [row for row in reader if row and row[0] != name_to_delete]

    with open(FILENAME, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(records)

    print (f"[{name_to_delete}] has been deleted successfully.")

def search_record():
    get_name = input("Enter name to get: ").title().strip()

    with open(FILENAME, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        records = list(reader)

    matches = [row for row in records if row["Name"] == get_name]

    if matches:
        print("======" * 6)
        for row in matches:
            print(f"{row['Name']} | {row['Item']} = {row['Price']} x {row['How Many?']} = {row['Total']}")
        print("======" * 6)
    else:
        print(f"No record found for '{get_name}'.")

def main():
    print ("Please wait, Checking file if it is already there..")
    time.sleep(1)

    if not os.path.exists(FILENAME):
        print("Creating file..")
        time.sleep(1)
        create_file()
        time.sleep(1)
        print("File has been created!")

    else:
        print("File already exists")
        time.sleep(1)

    print("=====" * 6)
    while True:
        time.sleep(1)
        print("Welcome To Utang Management System!")
        print("\n\t1. Create A Record")
        print("\t2. Read All Records")
        print("\t3. Search A Record")
        print("\t4. Delete A Record")
        print("\t5. Exit\n")
        try:
            choice = int(input("Please enter your choice (1-5): ").strip())
            print("")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_record()
        elif choice == 2:
            read_record()
        elif choice == 3:
            search_record()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()