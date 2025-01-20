import sqlite3

# функция создания таблицы
def create_db(): 
    connection = sqlite3.connect('my_database.db')  # утанавливаем и создает базу данных
    cursor = connection.cursor()  # устанавливаем курсор

    # создаем таблицу
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (  
                id INTEGER PRIMARY KEY,
                tg_id ITEXT NOT NULL,
                status_pars TEXT NOT NULL,
                count_pars INTEGER
    )''')  
    connection.commit()  
    connection.close()  


def reterner_col(col_name: tuple):  # возвращает значения из столбца col_name
    connect = sqlite3.connect('my_database.db')
    curs = connect.cursor()

    curs.execute('''SELECT *
                 FROM Users
                 WHERE tg_id = ?''',
                 col_name)
    
    lst = curs.fetchall()
    connect.close()

    return lst


# записываем новые строки в таблицу Users
def insert_datas(val: tuple) -> None:  
    con = sqlite3.connect('my_database.db')  # подключаемся к базе данных
    curs = con.cursor()  # устанавливаем курсор

    curs.execute('INSERT INTO Users (tg_id, status_pars, count_pars) VALUES(?, ?, ?)',  # (?, ?) ставится что бы потом по шаблону подать кортеж
                 val)  # val должен быть кортежем

    con.commit()  # применяем изменения
    con.close()  # закрываем соединение