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


def verification_mode(tg_id: str) -> bool:
    '''Проверяет какой режим парсинга установлен у пользователя'''
    connect = sqlite3.connect('./data/users.db')
    curs = connect.cursor()

    curs.execute('''SELECT in_pars
                 FROM Users
                WHERE tg_id = ?''',
                (tg_id, ) )
    
    lst = curs.fetchall()
    print(lst)
    connect.close()  # сразу закрывает базу что бы не забыть

    if 'true' in lst[0]:
        return True
    else:
        return False



def verification_user(tg_id: str) -> bool: 
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



def all_datas() -> bool:
    '''Возвращает все содержимое базы данных. просто чтобы можно было в консоле посмотреть содержимое базы'''
    connect = sqlite3.connect('./data/users.db')
    curs = connect.cursor()

    curs.execute('''SELECT *
                 FROM Users''')
    
    lst = curs.fetchall()
    connect.close()

    return lst


def set_pars_mode(tg_id: str, var: str='true'): 
    '''Функция выставляет режим парсинга. пр умолчанию true'''
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('./data/users.db')
    cursor = connection.cursor()

    # выставляет режим парсинга в true или false
    cursor.execute('UPDATE Users SET in_pars = ? WHERE tg_id = ?', (var, tg_id))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def set_wb_id(tg_id: str, wb_id:str): 
    '''Функция сохраняет запрашиваемые wb_id
    Записывает просто как стороку в которой через запятую идут все значения.
    Хорошо бы оптимизировать как нибудь'''
    # достает список id и добавляет к нему новый
    connection = sqlite3.connect('./data/users.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT wb_id
                 FROM Users
                WHERE tg_id = ?''',
                (tg_id, ) )
    lst = cursor.fetchall()  # все запрашиваемые пользователем id
    if lst:
        res = lst[0][0] + f", {wb_id}"  # все запрашиваемые пользователем id плюс новый через запятую
        #print(res)
        cursor.execute('UPDATE Users SET wb_id = ? WHERE tg_id = ?', (res, tg_id))  # запись значения в базу данных
        connection.commit()
    
        # прибавляет 1 + к количеству парсинга
        connection = sqlite3.connect('./data/users.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT count
                    FROM Users
                    WHERE tg_id = ?''',
                    (tg_id, ) )
        lst = cursor.fetchall()
        if lst:
            cnt = lst[0][0] + 1
            cursor.execute('UPDATE Users SET count = ? WHERE tg_id = ?', (cnt, tg_id))  # запись значения в базу данных
            connection.commit()
    connection.close()  # закрывает базу данных


#print(verification_user("14881488"))
#set_pars_mode("14881488", var="false")s


#print(verification_mode("14881488"))

#set_wb_id('14881488', wb_id="3221")
print(all_datas())