# Reflection

## 1. bugs

1. Artist search returned no matches for partial queries.
Expected: searching for `que` should match `Queen`.
Actual: search only matched when the full artist string appeared inside the query text.

2. Playlist stats were inconsistent.
Expected: hype ratio should be `hype_count / total_songs` and average energy should use all songs.
Actual: both were computed using only the Hype list in key places, producing misleading metrics.

3. Lucky pick crashed in empty scenarios.
Expected: empty source list should return no song and show a warning.
Actual: random choice on an empty list could raise an error.

## 2. How did you use AI as a teammate?

Correct suggestion:
- AI suggested reversing the search containment check from `value in query` to `query in value`.
- Why it was correct: this matches user intent for substring search.
- How I verified: added pytest case in `test/test_game_logic.py` for case-insensitive partial query and confirmed it passes.

Incorrect/misleading suggestion:
- AI initially focused only on search behavior and assumed that was the single bug being fixed.
- Why it was misleading: additional logic issues existed in stats and empty lucky pick behavior.
- How I corrected it: reviewed `playlist_logic.py` function by function, implemented targeted fixes, and expanded tests for each repaired behavior.

## 3. Debugging and testing your fixes

I verified repairs using a mix of unit tests and code review:

- Added tests for:
  - partial artist search (`search_songs`)
  - accurate stats calculation (`compute_playlist_stats`)
  - non-mutating playlist merge (`merge_playlists`)
  - empty random choice safety (`random_choice_or_none`)

- Test command used:
  - `pytest -q`

- Result:
  - all tests pass after fixes.

## Final Reflection

The most useful pattern was pairing AI-generated ideas with strict verification in tests. AI sped up pattern recognition and candidate fixes, but correctness still required careful human review of edge cases and metrics logic. I learned to treat AI as a collaborator for hypotheses, not as the final authority on behavior.
