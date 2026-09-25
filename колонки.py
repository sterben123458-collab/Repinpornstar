import sqlite3

db_path = '/Users/gosha/Documents/Учеба/python/hub2026/archive/database.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Запрашиваем информацию о колонках таблицы data_table
cursor.execute("PRAGMA table_info(data_table);")
columns = cursor.fetchall()

print("Колонки в базе данных:")
for col in columns:
    col_id, col_name, col_type, not_null, default_val, is_pk = col
    pk_str = " (Primary Key)" if is_pk else ""
    print(f"- {col_name} [{col_type}]{pk_str}")

conn.close()