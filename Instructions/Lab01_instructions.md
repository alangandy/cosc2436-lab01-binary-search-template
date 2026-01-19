# Lab 01: Binary Search

## Overview
In this lab, you will implement two fundamental search algorithms: **Linear Search** and **Binary Search**. These algorithms are covered in Chapter 1 of "Grokking Algorithms."

## Learning Objectives
- Understand the difference between O(n) and O(log n) time complexity
- Implement linear search for unsorted data
- Implement binary search for sorted data
- Compare the efficiency of both algorithms

## Background

### Linear Search - O(n)
Linear search checks each element one by one until it finds the target or reaches the end. It works on any list but can be slow for large datasets.

### Binary Search - O(log n)
Binary search uses divide and conquer on **sorted** data:
1. Check the middle element
2. If it's the target, done!
3. If target is smaller, search the left half
4. If target is larger, search the right half
5. Repeat until found or no elements left

**Key insight**: Binary search eliminates half the remaining elements with each comparison.

---

## Complete Solutions

### Task 1: `linear_search()` - Complete Implementation

```python
def linear_search(items: List[Dict], target_name: str) -> Tuple[Optional[Dict], int]:
    """
    Search for an item by name using linear search.
    
    Args:
        items: List of dictionaries with 'name' key
        target_name: Name to search for (case-insensitive)
    
    Returns:
        Tuple of (found item or None, number of comparisons)
    
    Time Complexity: O(n)
    """
    comparisons = 0
    target_lower = target_name.lower()
    
    for item in items:
        comparisons += 1
        if item["name"].lower() == target_lower:
            return (item, comparisons)
    
    return (None, comparisons)
```

**How it works:**
1. Convert target to lowercase for case-insensitive comparison
2. Loop through each item in the list
3. Increment the comparison counter for each item checked
4. If the item's name matches (case-insensitive), return the item and count
5. If we reach the end without finding it, return `(None, comparisons)`

---

### Task 2: `binary_search()` - Complete Implementation

```python
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
    """
    comparisons = 0
    left = 0
    right = len(sorted_items) - 1
    target_lower = target_name.lower()
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        mid_name = sorted_items[mid]["name"].lower()
        
        if mid_name == target_lower:
            return (sorted_items[mid], comparisons)
        elif mid_name < target_lower:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return (None, comparisons)
```

**How it works:**
1. Initialize `left` to 0 and `right` to the last index
2. Convert target to lowercase for case-insensitive comparison
3. While `left <= right` (there's still a range to search):
   - Calculate the middle index: `mid = (left + right) // 2`
   - Increment the comparison counter
   - Compare the middle item's name with the target:
     - If equal: found it! Return the item and count
     - If middle < target: target is in the right half, so `left = mid + 1`
     - If middle > target: target is in the left half, so `right = mid - 1`
4. If the loop ends without finding, return `(None, comparisons)`

---

## Example Usage

```python
# Sample data
cities = [
    {"name": "Austin", "population": 964254},
    {"name": "Dallas", "population": 1304379},
    {"name": "Houston", "population": 2304580},
    {"name": "San Antonio", "population": 1547253}
]

# Linear search (works on any list)
result, comparisons = linear_search(cities, "Houston")
print(f"Found: {result['name']}, Comparisons: {comparisons}")
# Output: Found: Houston, Comparisons: 3

# Binary search (requires sorted list)
sorted_cities = sorted(cities, key=lambda x: x["name"].lower())
result, comparisons = binary_search(sorted_cities, "Houston")
print(f"Found: {result['name']}, Comparisons: {comparisons}")
# Output: Found: Houston, Comparisons: 2
```

---

## Testing
Run the tests to verify your implementation:
```bash
python -m pytest tests/ -v
```

## Submission
Commit and push your completed `search.py` file.
