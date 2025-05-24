import csv
import datetime
import os
import time
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas


FILENAME = "receipt.csv"
HEADER = ["Name", "Container", "Price", "Total", "Timestamp"]


def create_file():

    with open(FILENAME, "w", newline = "") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(HEADER)

def add_order():

    with open(FILENAME, "a", newline = "") as csv_file:
        writer = csv.writer(csv_file)

        print ("------" * 6, "\n")

        name = input("Name: ").strip().title()

        while True:
            try:
                con = int(input("How many container? ").strip())
                break

            except ValueError:
                print("Invalid Input, Please try again.")
                continue

        price = int(input("Price: "))
        total = int(con) * int(price)
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow([name, con, price, total, now_str])

        time.sleep(1)

        return name, con, price, total, now_str


def view_order():

    print ("\n\t\t  |Order History|")
    print ("======" * 6)

    with open(FILENAME, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        records = list(reader)

        if records:
            for row in records:
                print(f"Name: {row["Name"]}, Containers: {row["Container"]}, Price: ₱{row["Price"]}, Total: ₱{row["Total"]}, Timestamp: {row["Timestamp"]}")
        else:
            print ("\t\tThere are no Records")

    print("======" * 6)
    time.sleep(1)

def print_order(name, con, price, total, now_str):

    pdf_folder = "receipts"
    os.makedirs(pdf_folder, exist_ok=True)
    filename = os.path.join(pdf_folder, f"receipt_{now_str.replace(':', ' ').replace('-', ' ').replace(' ', '_')}.pdf")

    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y, "Water Refilling Station Receipt")

    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Date & Time: {now_str}")
    y -= 20
    c.drawString(50, y, f"Customer Name: {name}")
    y -= 20
    c.drawString(50, y, f"Containers: {con}")
    y -= 20
    c.drawString(50, y, f"Price per Container: ₱{price}")
    y -= 20
    c.drawString(50, y, f"Total: ₱{total}")
    y -= 40
    c.drawString(50, y, "Thank you for your order!")

    c.save()

    print(f"\nReceipt saved as: {filename}")

    try:
        os.startfile(filename, "print")
    except Exception as e:
        print("Could not print automatically:", e)
        
def main():

    if not os.path.exists(FILENAME):
        create_file()
        print("file has been created")
    else:
        print("There is already a file")

    print ("======" * 6)

    while True:
        print ("")
        print ("\t  Welcome to Order System!")
        print ("")
        print ("------" * 6)
        print ("")
        print ("\t\t1. Create an Order")
        print ("\t\t2. View Order History")
        print ("\t\t3. Exit")
        print ("")
        print ("------" * 6)

        try:
            choice = int(input("\tChoice: ").strip())

        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        if choice == 1:

            result = add_order()

            if result:
                name, con, price, total, now_str = result
                print_order(name, con, price, total, now_str)

        elif choice == 2:
            view_order()

        elif choice == 3:
            print ("------" * 6, "\n")
            print("\t\t\t GoodBye!\n")
            print ("------" * 6)
            break

if __name__ == "__main__":
    main()
