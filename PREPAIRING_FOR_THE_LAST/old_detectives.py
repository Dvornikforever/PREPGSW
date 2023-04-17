# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

result = cur.execute("""SELECT title FROM films WHERE year BETWEEN 1995 AND 2000
 AND genre IN (SELECT id FROM genres WHERE title = 'детектив')""")

for elem in result:
    print(elem[0])

con.close()
