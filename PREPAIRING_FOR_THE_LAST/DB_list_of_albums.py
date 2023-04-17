import sqlite3

con = sqlite3.connect('Chinook_Sqlite.sqlite')

cur = con.cursor()

result = cur.execute("""SELECT
    Album.Title
FROM
    Album
LEFT JOIN Album ON Track.AlbumId = Album.AlbumId
ORDER BY Album.ArtistId""").fetchall()

for elem in result:
    print(elem[0])

con.close()
