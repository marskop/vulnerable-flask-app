import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Δημιουργία πίνακα χρηστών
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Προσθήκη κάποιων χρηστών
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpassword')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
