from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums
    
    def find(self):
        user_input_album_id = input('Enter an album id')
        row = self._connection.execute(f'SELECT * FROM albums WHERE id = {user_input_album_id}')[0]
        return Album(row['id'], row['title'], row['release_year'], row['artist_id'])
