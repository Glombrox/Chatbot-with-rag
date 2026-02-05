import sqlite3
from config import DB_PATH 

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("DELETE FROM messages")
conn.commit()
conn.close()

print("All messages deleted from the database.")