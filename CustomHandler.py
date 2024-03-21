import logging
import sqlite3

class CustomHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        # Connect to the database
        self.conn = sqlite3.connect('logs.db')
        self.create_table()

    def create_table(self):
        # Create a table if it doesn't exist
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP,
                name TEXT,
                level TEXT,
                message TEXT
            )
        ''')
        self.conn.commit()

    def emit(self, record):
        log_entry = self.format(record)
        
        # Insert log entry into the database
        self.conn.execute('''
            INSERT INTO logs (timestamp, name, level, message)
            VALUES (?,?,?,?)
        ''', (record.created, record.name, record.levelname, record.msg))
        self.conn.commit()

        print("Custom Handler: ", log_entry)

    def close(self):
        # Close database connection
        self.conn.close()
