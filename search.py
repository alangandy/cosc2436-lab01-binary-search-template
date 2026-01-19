"""
Lab 01: Search Algorithms
Implement linear search and binary search.

From Chapter 1 of "Grokking Algorithms":
- Linear search: O(n) - check each element one by one
- Binary search: O(log n) - divide and conquer on sorted data
"""
from typing import List, Dict, Optional, Tuple


def linear_search(items: List[Dict], target_name: str) -> Tuple[Optional[Dict], int]:
    """
    Search for an item by name using linear search.
    
    Args:
        items: List of dictionaries with 'name' key
        target_name: Name to search for (case-insensitive)
    
    Returns:
        Tuple of (found item or None, number of comparisons)
    
    Time Complexity: O(n)
    
    Example:
        >>> cities = [{"name": "Houston"}, {"name": "Dallas"}]
        >>> result, comparisons = linear_search(cities, "Dallas")
        >>> result["name"]
        'Dallas'
        >>> comparisons
        2
    """
    comparisons = 0
    
    # TODO: Implement linear search
    # 1. Loop through each item in the list
    # 2. Increment comparisons counter
    # 3. Check if item's name matches target (case-insensitive)
    # 4. Return (item, comparisons) if found
    # 5. Return (None, comparisons) if not found
    
    pass  # Remove this and add your code


def binary_search(sorted_items: List[Dict], target_name: str) -> Tuple[Optional[Dict], int]:
    """
    Search for an item by name using binary search.
    REQUIRES: sorted_items must be sorted alphabetically by name!
    
    Args:
        sorted_items: List of dictionaries sorted by 'name' key
        target_name: Name to search for (case-insensitive)
    
    Returns:
        Tuple of (found item or None, number of comparisons)
    
    Time Complexity: O(log n)
    
    Example:
        >>> cities = [{"name": "Austin"}, {"name": "Dallas"}, {"name": "Houston"}]
        >>> result, comparisons = binary_search(cities, "Dallas")
        >>> result["name"]
        'Dallas'
    """
    comparisons = 0
    left = 0
    right = len(sorted_items) - 1
    target_lower = target_name.lower()
    
    # TODO: Implement binary search
    # 1. While left <= right:
    #    a. Calculate mid index
    #    b. Increment comparisons
    #    c. Compare mid item's name with target
    #    d. If equal, return (item, comparisons)
    #    e. If mid < target, search right half (left = mid + 1)
    #    f. If mid > target, search left half (right = mid - 1)
    # 2. Return (None, comparisons) if not found
    
    pass  # Remove this and add your code
