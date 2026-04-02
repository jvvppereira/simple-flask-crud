# Simple Flask Transaction CRUD

A lightweight Flask web application for managing financial transactions. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using Python and Flask, with in-memory data storage.

## 🚀 Features

- **Read**: View a comprehensive list of all transactions.
- **Create**: Add new transactions with a date and amount.
- **Update**: Edit existing transactions to correct or update details.
- **Delete**: Remove transactions from the record.
- **Search**: Filter transactions according to a specific amount range (minimum and maximum).
- **Balance Calculation**: Automatically calculate and display the total balance of all recorded transactions.

## 🛠️ Technologies Used

- **Python 3**
- **Flask**: A lightweight WSGI web application framework.
- **Jinja2**: Templating engine for Python.
- **HTML/CSS**: For the front-end interface.

## 📂 Project Structure

```text
simple-flask-crud/
├── app.py              # Main application file with routes and logic
├── templates/          # HTML templates folder
│   ├── transactions.html   # Main dashboard for listing transactions
│   ├── form.html           # Interface to add new transactions
│   ├── edit.html           # Interface to update existing transactions
│   └── search.html         # Interface for filtering transactions
└── README.md           # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd simple-flask-crud
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install Flask
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to: `http://127.0.0.1:5000/`

## 📝 Usage

- **Home Page**: Displays all transactions and the navigation menu.
- **Add Transaction**: Click the "Add Transaction" link to fill out a form with the date and amount.
- **Edit/Delete**: Use the links provided next to each transaction in the list to modify or remove them.
- **Search**: Navigate to the search page to filter transactions by their value.
- **Total Balance**: Access the `/balance` route to see the cumulative total of all transactions.

---
*Created as part of a Python development practice project.*
