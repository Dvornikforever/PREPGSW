# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect('Chinook_Sqlite.sqlite')

# Создание курсора
cur = con.cursor()

result = cur.execute("""SELECT
    Track.Name as TrackName,
    Genre.Name as GenreName,
    Album.Title as AlbumTitle,
    Artist.Name
FROM
    Track
LEFT JOIN Genre ON Track.GenreId = Genre.GenreId
LEFT JOIN Album ON Track.AlbumId = Album.AlbumId
LEFT JOIN Artist ON Album.ArtistId = Artist.ArtistId
ORDER BY TrackName""").fetchall()

for elem in result:
    print(elem[0])

con.close()
