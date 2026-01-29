"""
Lab 01: Test Cases for Search Algorithms
Run with: python -m pytest tests/ -v
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from search import linear_search, binary_search


# Test data
CITIES = [
    {"name": "Austin", "population": 978908},
    {"name": "Dallas", "population": 1304379},
    {"name": "Houston", "population": 2304580},
    {"name": "Plano", "population": 287677},
    {"name": "San Antonio", "population": 1547253},
]

CITIES_SORTED = sorted(CITIES, key=lambda x: x['name'].lower())


class TestLinearSearch:
    def test_find_first_element(self):
        """Should find element at beginning of list."""
        result, comparisons = linear_search(CITIES, "Austin")
        assert result is not None
        assert result["name"] == "Austin"
        assert comparisons >= 1

    def test_find_last_element(self):
        """Should find element at end of list."""
        result, comparisons = linear_search(CITIES, "San Antonio")
        assert result is not None
        assert result["name"] == "San Antonio"

    def test_find_middle_element(self):
        """Should find element in middle of list."""
        result, comparisons = linear_search(CITIES, "Houston")
        assert result is not None
        assert result["name"] == "Houston"

    def test_not_found(self):
        """Should return None for non-existent element."""
        result, comparisons = linear_search(CITIES, "Chicago")
        assert result is None
        assert comparisons == len(CITIES)  # Should check all elements

    def test_case_insensitive(self):
        """Should find element regardless of case."""
        result, _ = linear_search(CITIES, "houston")
        assert result is not None
        assert result["name"] == "Houston"

        result, _ = linear_search(CITIES, "DALLAS")
        assert result is not None
        assert result["name"] == "Dallas"

    def test_empty_list(self):
        """Should handle empty list."""
        result, comparisons = linear_search([], "Houston")
        assert result is None
        assert comparisons == 0

    def test_returns_correct_data(self):
        """Should return the complete dictionary."""
        result, _ = linear_search(CITIES, "Houston")
        assert result["name"] == "Houston"
        assert result["population"] == 2304580


class TestBinarySearch:
    def test_find_middle_element(self):
        """Should find element in middle (best case)."""
        result, comparisons = binary_search(CITIES_SORTED, "Houston")
        assert result is not None
        assert result["name"] == "Houston"
        assert comparisons >= 1

    def test_find_first_element(self):
        """Should find element at beginning."""
        result, comparisons = binary_search(CITIES_SORTED, "Austin")
        assert result is not None
        assert result["name"] == "Austin"

    def test_find_last_element(self):
        """Should find element at end."""
        result, comparisons = binary_search(CITIES_SORTED, "San Antonio")
        assert result is not None
        assert result["name"] == "San Antonio"

    def test_not_found(self):
        """Should return None for non-existent element."""
        result, comparisons = binary_search(CITIES_SORTED, "Chicago")
        assert result is None

    def test_case_insensitive(self):
        """Should find element regardless of case."""
        result, _ = binary_search(CITIES_SORTED, "houston")
        assert result is not None
        assert result["name"] == "Houston"

    def test_empty_list(self):
        """Should handle empty list."""
        result, comparisons = binary_search([], "Houston")
        assert result is None
        assert comparisons == 0

    def test_single_element_found(self):
        """Should work with single element list."""
        single = [{"name": "Houston", "population": 2304580}]
        result, comparisons = binary_search(single, "Houston")
        assert result is not None
        assert comparisons == 1

    def test_single_element_not_found(self):
        """Should work with single element list when not found."""
        single = [{"name": "Houston", "population": 2304580}]
        result, comparisons = binary_search(single, "Dallas")
        assert result is None

    def test_efficiency(self):
        """Binary search should use O(log n) comparisons."""
        # For 5 elements, should need at most 3 comparisons (log2(5) ≈ 2.3)
        result, comparisons = binary_search(CITIES_SORTED, "Plano")
        assert comparisons <= 3


class TestSearchComparison:
    def test_both_find_same_result(self):
        """Both algorithms should find the same item."""
        linear_result, _ = linear_search(CITIES, "Dallas")
        binary_result, _ = binary_search(CITIES_SORTED, "Dallas")

        assert linear_result["name"] == binary_result["name"]
        assert linear_result["population"] == binary_result["population"]

    def test_binary_uses_fewer_comparisons(self):
        """Binary search should use fewer comparisons on larger lists."""
        # Create larger list
        large_list = [{"name": f"City{i:04d}"} for i in range(1000)]
        large_sorted = sorted(large_list, key=lambda x: x['name'])

        _, linear_comps = linear_search(large_list, "City0500")
        _, binary_comps = binary_search(large_sorted, "City0500")

        assert binary_comps < linear_comps


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
