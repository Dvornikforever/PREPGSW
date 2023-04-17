# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

result = cur.execute("""SELECT title FROM genres
 WHERE id IN (SELECT DISTINCT genre FROM films WHERE year IN (2010, 2011))""").fetchall()

for elem in result:
    print(elem[0])

con.close()
