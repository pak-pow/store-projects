# utang / bale management

05 / 23 / 2025 

🧾 Utang Management System
- A simple command-line-based debt and sales tracking system built using Python.
- This tool was created to support my family's store by making it easier to record, search, view, and manage item transactions and customer debts.

💡 Why I Built This
- Managing a small business can be challenging, especially when it comes to tracking customers' purchases and debts
- To help my family stay organized and reduce manual record-keeping, I created this lightweight system that uses a CSV file to store and retrieve data efficiently.

📋 Features
- Create Records: Add a new entry for customer purchases including name, item, price, quantity, total cost, and timestamp.
- View All Records: List all the stored transactions in a readable format.
- Search Records: Find purchases by a customer’s name.
- Delete Records: Remove a customer’s entry from the file.
- CSV File-Based Storage: All data is saved in a bale.csv file, so it’s portable and easy to back up.

⚙️ How It Works
When you run the script:

- It checks if the file bale.csv exists.
- If not, it creates it and adds headers.
- It displays a menu where you can:
  - Add a new record
  - View all existing records
  - Search by customer name
  - Delete a record by customer name
  - Exit the program

🛠️ Requirements
- Python 3.x
- No third-party libraries are required; everything is built using Python's built-in modules.

📌 Notes
- All numeric inputs must be valid numbers.

[The system is designed for small-scale use and stores data in a simple CSV format for ease of use and accessibility.]
