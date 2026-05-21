"""
init_db.py — Database initialisation for Bin Khalid Dairy Farm
Run once:  python init_db.py
"""

import sqlite3

DB_PATH = "database.db"


def init_database():
    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vouchers (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT    NOT NULL,
            date       TEXT    NOT NULL,
            days       INTEGER NOT NULL DEFAULT 0,
            rate       REAL    NOT NULL DEFAULT 0.0,
            daily      REAL    NOT NULL DEFAULT 0.0,
            extra      REAL    NOT NULL DEFAULT 0.0,
            used       REAL    NOT NULL DEFAULT 0.0,
            due        REAL    NOT NULL DEFAULT 0.0,
            total_milk REAL    NOT NULL DEFAULT 0.0,
            amount     REAL    NOT NULL DEFAULT 0.0,
            final_bill REAL    NOT NULL DEFAULT 0.0,
            created_at TEXT    DEFAULT (datetime('now'))
        )
    """)

    conn.commit()
    conn.close()
    print("✅  database.db initialised successfully.")


if __name__ == "__main__":
    init_database()