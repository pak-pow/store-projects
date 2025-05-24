# 💧 Water Refilling Station Receipt Maker

A simple Python terminal-based application designed to create, save, and display receipts for a water refilling station. It logs customer orders in a CSV file and provides a printed slip for each transaction.

---

## 📂 Features

- 📦 **Order Creation**: Enter customer name, number of containers, and price.
- 🧾 **Receipt Generation**: Print a formatted receipt with timestamp.
- 🗃️ **Order History**: View all past transactions stored in a CSV file.
- 💾 **Data Persistence**: Saves all records in `receipt.csv`.

---

## 🛠️ How It Works

1. **Startup**: Checks for `receipt.csv`; creates it if missing.
2. **User Menu**:
   - `1. Create an Order`
   - `2. View Order History`
   - `3. Exit`
3. **CSV Format**: 
   ```csv
   Name,Container,Price,Total,Timestamp
   ```

---

## 🖥️ Requirements

- Python 3.x
- No external libraries (uses standard library only)

---

## 🚀 Running the Program

```bash
python receipt_maker.py
```

Follow the on-screen instructions to create orders or view order history.

---

## 📁 File Structure

```
receipt_maker.py       # Main application script
receipt.csv            # CSV log file (created on first run)
```

---

## 🔐 Notes

- Input validation is included for numerical entries.
- The script uses `time.sleep(1)` for a smooth user experience.
- Timestamps follow the format `YYYY-MM-DD HH:MM:SS`.

---

## 📄 Example Output

```
Customer:                      Juan Dela Cruz
Container:                     3
Price:                         25
Total:                         75
Timestamp:                     2025-05-24 14:30:10
```
