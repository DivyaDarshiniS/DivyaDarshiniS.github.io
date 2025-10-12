import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Tests that the longest streak is returned when there are multiple."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 0, 1]) == 3

def test_with_zeros_and_negatives():
    """Tests that zeros and negative numbers break the streak."""
    assert longest_positive_streak([1, -2, 3, 4, 0, 5, 6, 7, 8, -1, 2]) == 4

def test_all_positives():
    """Tests a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_no_positives():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -4, -5]) == 0
