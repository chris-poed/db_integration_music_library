from pytest import mark

from lib.album import Album

@mark.it('Test album construct with title, release_year, and artist_id')
def test_album_constructs():
    album = Album(1, "Test Album", "Test release year", 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == "Test release year"
    assert album.artist_id == 1