import sqlite3
from datetime import date
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")
@mcp.tool
def addExpense(
    price: int,
    category: str,
    description: str,
    date_spent: str = "",
    payment_method: str = "",
    notes: str = ""
) -> dict:
    """Record a new expense in the user's expense tracker.

    Use this tool whenever the user wants to log money they have spent.
    Accept the amount in rupees, category, and description.
    Optionally accept the transaction date, payment method, and notes.
    If the date is not provided, use today's date.
    Save the expense in the database and return its ID and confirmation.
    """

    if price <= 0:
        return {"success": False, "error": "Price must be greater than zero."}

    if not category.strip() or not description.strip():
        return {"success": False, "error": "Category and description are required."}

    if not date_spent:
        date_spent = date.today().isoformat()

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price INTEGER NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            date_spent TEXT NOT NULL,
            payment_method TEXT,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        INSERT INTO expenses (
            price, category, description, date_spent,
            payment_method, notes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        price, category.strip(), description.strip(), date_spent,
        payment_method, notes
    ))

    expense_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        "success": True,
        "expense_id": expense_id,
        "price": price,
        "category": category,
        "description": description,
        "date": date_spent,
        "message": "Expense saved successfully."
    }



@mcp.tool
def ListExpense(start_date: str, end_date: str) -> dict:
    """List expense entries within an inclusive date range.

    Use this tool when the user wants to view expenses between two dates.
    Accepts a start date and end date in YYYY-MM-DD format.
    Include expenses occurring on both the start date and end date.
    Retrieve the matching entries from the database, ordered by date
    from newest to oldest.
    Return the expense details and the total number of entries.
    in the way they want default use tabular way
    """

    import sqlite3
    from datetime import date

    if not start_date or not end_date:
        return {"success": False, "error": "Both dates are required."}

    try:
        start = date.fromisoformat(start_date)
        end = date.fromisoformat(end_date)
    except ValueError:
        return {"success": False, "error": "Dates must use YYYY-MM-DD format."}

    if start > end:
        return {"success": False, "error": "Start date must not be after end date."}

    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, price, category, description, date_spent,
                   payment_method, notes, created_at
            FROM expenses
            WHERE date_spent >= ? AND date_spent <= ?
            ORDER BY date_spent DESC, id DESC
        """, (start_date, end_date))

        expenses = [dict(row) for row in cursor.fetchall()]

        return {
            "success": True,
            "count": len(expenses),
            "expenses": expenses
        }
    finally:
        conn.close()
    

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
