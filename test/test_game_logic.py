from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from playlist_logic import search_songs


def test_search_songs_matches_partial_artist_query_case_insensitive():
    songs = [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "rock", "energy": 8},
        {"title": "Take Five", "artist": "Dave Brubeck", "genre": "jazz", "energy": 4},
    ]

    result = search_songs(songs, "  QUE  ", field="artist")

    assert len(result) == 1
    assert result[0]["artist"] == "Queen"
