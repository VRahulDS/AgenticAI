import sqlite3
from rag_paths import DB_DIR
import os

db_path = os.path.join(DB_DIR, "chroma.sqlite3")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM embeddings;")

tables = cursor.fetchall()
print(tables)