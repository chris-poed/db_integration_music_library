import builtins

from pytest import MonkeyPatch, mark

from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository #all
We get a list of Album objects reflecting the seed data
"""

@mark.it('#all returns a list of all Album objects reflecting the seed data')
def test_get_all_records(db_connection):
        db_connection.seed("seeds/music_library.sql")
        repository = AlbumRepository(db_connection)
        albums = repository.all()

        assert albums == [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1),
            Album(3, "Waterloo", 1974, 2),
            Album(4, "Super Trouper", 1980, 2),
            Album(5, "Bossanova", 1990, 1),
            Album(6, "Lover", 2019, 3),
            Album(7, "Folklore", 2020, 3),
            Album(8, "I Put a Spell on You", 1965, 4),
            Album(9, "Baltimore", 1978, 4),
            Album(10, "Here Comes the Sun", 1971, 4),
            Album(11, "Fodder on My Wings", 1982, 4),
            Album(12, "Ring Ring", 1973, 2),
        ]

@mark.it('#find returns a single album when passed an id')
def test_find_album_from_id(db_connection, monkeypatch):
        monkeypatch.setattr(builtins, "input", lambda _: "12") # Arrange: fake user input
        db_connection.seed("seeds/music_library.sql")
        repository = AlbumRepository(db_connection)
        album = repository.find()
        assert album == Album(12, 'Ring Ring', 1973, 2)