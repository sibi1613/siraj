from database.database import get_connection
import sqlite3


def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users(username, password)
            VALUES (?, ?)
        """, (username, password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user