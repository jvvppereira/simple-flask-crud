# Import libraries
from flask import Flask, render_template, request, url_for, redirect 

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
            }
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    
    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    found = next((t for t in transactions if t["id"]==transaction_id), None)
    if request.method == 'GET':
        if found:
            return render_template("edit.html", transaction=found)
    if request.method == 'POST':
        if found:
            date = request.form['date']           # Get the 'date' field value from the form
            amount = float(request.form['amount'])# Get the 'amount' field value from the form and convert it to a float
    
            found['date'] = date       # Update the 'date' field of the transaction
            found['amount'] = amount   # Update the 'amount' field of the transaction
            
            return redirect(url_for("get_transactions"))

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    found = next((t for t in transactions if t["id"]==transaction_id), None)
    if found:
        transactions.remove(found)
        return redirect(url_for("get_transactions"))

@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == 'POST':
        minimum = float(request.form['min_amount'])
        maximum = float(request.form['max_amount'])
        filtered_transactions = list(filter(lambda t:  t["amount"]>minimum and t["amount"]<maximum, transactions)) 
        return render_template("transactions.html", transactions=filtered_transactions)
    if request.method == 'GET':
        return render_template("search.html")

@app.route("/balance")
def total_balance():
    balance = 0
    for transaction in transactions:
        balance += transaction["amount"]
    return render_template("transactions.html", transactions=transactions, balance=balance)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
