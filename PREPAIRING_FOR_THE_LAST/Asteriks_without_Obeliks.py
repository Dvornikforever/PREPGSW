# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

result = cur.execute("""SELECT title FROM films WHERE title like '%Астерикс%' AND title not like '%Обеликс%'""")

for elem in result:
    print(elem[0])

con.close()
