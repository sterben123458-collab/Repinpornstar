import os
import sqlite3
import pandas as pd
from eralchemy2 import render_er

# Путь к вашей папке
folder_path = '/Users/gosha/Documents/Учеба/python/hub2026/archive'

# Автоматически ищем первый попавшийся файл с расширением .csv в папке
csv_filename = None
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        csv_filename = file
        break

if not csv_filename:
    raise FileNotFoundError(f'В папке {folder_path} не найден ни один CSV-файл!')

print(f'Найден файл датасета: {csv_filename}')

# Названия файлов базы данных и картинки
db_filename = 'database.db'
output_image = 'database_model.png'

# Полные пути к файлам
csv_file_path = os.path.join(folder_path, csv_filename)
db_file_path = os.path.join(folder_path, db_filename)
output_image_path = os.path.join(folder_path, output_image)

table_name = 'data_table'  # Название таблицы в базе данных

def create_db_from_csv():
    print('1. Загружаем датасет и создаем базу данных...')
    
    # Загружаем данные с помощью pandas
    df = pd.read_csv(csv_file_path)
    
    # Подключаемся к SQLite (файл создастся внутри вашей папки)
    conn = sqlite3.connect(db_file_path)
    
    # Записываем датафрейм в таблицу базы данных
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()
    print(f'Таблица "{table_name}" успешно создана в базе: {db_file_path}')

def draw_database_model():
    print('2. Генерируем ER-диаграмму базы данных...')
    
    # Формируем строку подключения для eralchemy2
    sqlite_uri = f'sqlite:///{db_file_path}'
    
    # Рисуем и сохраняем схему в графический файл в ту же папку
    render_er(sqlite_uri, output_image_path)
    print(f'Модель базы данных сохранена в файл: {output_image_path}')
 
if __name__ == '__main__':
    try:
        create_db_from_csv()
        draw_database_model()
        print('Все задачи выполнены успешно!')
    except Exception as e:
        print(f'Произошла ошибка: {e}')