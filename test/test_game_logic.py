from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from playlist_logic import (
    compute_playlist_stats,
    merge_playlists,
    random_choice_or_none,
    search_songs,
)


def test_search_songs_matches_partial_artist_query_case_insensitive():
    songs = [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "rock", "energy": 8},
        {"title": "Take Five", "artist": "Dave Brubeck", "genre": "jazz", "energy": 4},
    ]

    result = search_songs(songs, "  QUE  ", field="artist")

    assert len(result) == 1
    assert result[0]["artist"] == "Queen"


def test_compute_playlist_stats_uses_all_songs_for_hype_ratio_and_average_energy():
    playlists = {
        "Hype": [{"title": "A", "artist": "x", "energy": 8}],
        "Chill": [{"title": "B", "artist": "y", "energy": 2}],
        "Mixed": [{"title": "C", "artist": "z", "energy": 5}],
    }

    stats = compute_playlist_stats(playlists)

    assert stats["total_songs"] == 3
    assert stats["hype_ratio"] == (1 / 3)
    assert stats["avg_energy"] == 5.0


def test_merge_playlists_does_not_mutate_inputs():
    a = {"Hype": [{"title": "A"}], "Chill": [], "Mixed": []}
    b = {"Hype": [{"title": "B"}]}

    merged = merge_playlists(a, b)
    merged["Hype"].append({"title": "C"})

    assert len(a["Hype"]) == 1
    assert len(b["Hype"]) == 1


def test_random_choice_or_none_returns_none_for_empty_list():
    assert random_choice_or_none([]) is None
