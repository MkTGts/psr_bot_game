import sqlite3


def create_db() -> None:
    '''Функция создает базу данных'''
    connection = sqlite3.connect('./data/users.db')  # утанавливаем и создает базу данных
    cursor = connection.cursor()  # устанавливаем курсор

    # создаем таблицу
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (  
                id INTEGER PRIMARY KEY,
                tg_id TEXT NOT NULL,
                in_pars TEXT NOT NULL,
                wb_id TEXT NOT NULL,
                count INTEGER
    )''')  
    connection.commit()  # выполняем изменения(совершаем)
    connection.close()  # закрываем соединение


def insert_datas(val: tuple[str, str, str, int]) -> None:  
    '''Функция заносит значения базу данных
    На вход принимает кортеж значений (in_pars, tg_id, wb_id, count)'''
    con = sqlite3.connect('./data/users.db')  # подключаемся к базе данных
    curs = con.cursor()  # устанавливаем курсор

    curs.execute('INSERT INTO Users (in_pars, tg_id, wb_id, count) VALUES(?, ?, ?, ?)',  # (?, ?) ставится что бы потом по шаблону подать кортеж
                 val)  # val должен быть кортежем

    con.commit()  # применяем изменения
    con.close()  # закрываем соединение


#create_db()
#insert_datas(("false", "14881488","159753456", 0))


def verification(tg_id: str) -> bool:
    '''Проверяет есть ли пользователь с таким id в базе данных'''
    connect = sqlite3.connect('./data/users.db')
    curs = connect.cursor()

    curs.execute('''SELECT tg_id
                 FROM Users
                WHERE tg_id = ?''',
                (tg_id, ) )
    
    lst = curs.fetchall()
    connect.close()

    return bool(lst)


def updater_datas():  # обновление записей
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Обновляем возраст пользователя "newuser"
    cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


#print(verification("14881488"))