import sqlite3
import os

DATABASE_NAME = os.path.join(os.path.dirname(__file__), "expense_tracker.db")


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn