import os
import sqlite3
import pandas as pd

# Путь к папке и базе данных
folder_path = '/Users/gosha/Documents/Учеба/python/hub2026/archive'
db_file_path = os.path.join(folder_path, 'database.db')

def run_sql_queries():
    # Подключаемся к базе данных SQLite
    conn = sqlite3.connect(db_file_path)
    
    print("=" * 50)
    print("1. Выборка первых 5 строк (базовый просмотр)")
    print("=" * 50)
    query_1 = "SELECT * FROM data_table LIMIT 5;"
    df_1 = pd.read_sql(query_1, conn)
    print(df_1, "\n")
    
    print("=" * 50)
    print("2. Сортировка данных по колонке \"2\" по убыванию")
    print("=" * 50)
    try:
        # Обратите внимание, что числовые имена колонок обязательно берутся в двойные кавычки
        query_2 = 'SELECT * FROM data_table ORDER BY "2" DESC LIMIT 5;'
        df_2 = pd.read_sql(query_2, conn)
        print(df_2, "\n")
    except Exception as e:
        print(f"Ошибка при сортировке: {e}\n")
        
    print("=" * 50)
    print("3. Группировка и подсчет строк по текстовой колонке \"1\"")
    print("=" * 50)
    try:
        query_3 = '''
            SELECT "1", COUNT(*) as total_count 
            FROM data_table 
            GROUP BY "1" 
            ORDER BY total_count DESC 
            LIMIT 5;
        '''
        df_3 = pd.read_sql(query_3, conn)
        print(df_3, "\n")
    except Exception as e:
        print(f"Ошибка при группировке: {e}\n")
        
    # Закрываем соединение с базой
    conn.close()
    print("Все запросы выполнены!")

if __name__ == '__main__':
    run_sql_queries()