# Personal Expense Tracker - Expense Tracking Version 1

This project is for personal use and is designed as a simple expense tracking application for managing personal spending. Expense Tracking Version 1 focuses on easy expense logging, category-based organization, and date-based reporting in a lightweight and practical setup.

## Overview

This application allows you to:

- Log individual expenses with amount, category, description, and date
- Track payment method and notes for each transaction
- View expenses within a custom date range
- Keep spending organized in a local SQLite database
- Run the tracker as a lightweight FastMCP service

The goal of this version is to provide a clean and practical starting point for personal expense tracking without unnecessary complexity.

## Features

- Expense entry management
- Category-based organization
- Optional payment method and note fields
- Date-based filtering and summaries
- Persistent storage using SQLite
- Simple local deployment
- Built in Python for easy customization

## Project Details

- Name: Personal Expense Tracker
- Version: 1
- Use case: Personal expense tracking
- Storage: SQLite database (`expenses.db`)
- Backend: Python + FastMCP

## Tech Stack

- Python 3.11+
- SQLite
- FastMCP

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd "Expense Tracker"
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastmcp
   ```

4. Start the app:
   ```bash
   python server.py
   ```

The service will run on:

- Host: `0.0.0.0`
- Port: `8000`

## Usage

The project exposes tools for managing expenses:

### Add an expense

Use the `addExpense` tool to save a new expense entry.

Example input:

- `price`: `350`
- `category`: `Food`
- `description`: `Lunch with client`
- `date_spent`: `2026-10-24`
- `payment_method`: `Card`
- `notes`: `Team lunch`

### List expenses by date range

Use the `ListExpense` tool to retrieve expenses between two dates.

Example input:

- `start_date`: `2026-10-01`
- `end_date`: `2026-10-31`

This returns the matching records and the total count for the selected range.

## Data Storage

The application stores transactions in a local SQLite database file named `expenses.db`.

## Notes

This project is for personal use and is designed as a practical expense tracking solution for everyday personal budgeting and review. It is currently version 1 and may be expanded in future versions with additional reporting and dashboard features.

## License

This project is intended for personal use and is not currently published as a commercial product.
