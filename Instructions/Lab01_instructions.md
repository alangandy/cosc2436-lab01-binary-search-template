# Lab 1: Introduction to Algorithms - Binary Search

## 1. Introduction and Objectives

### Overview
Implement linear search and binary search algorithms in Python using a dataset of Texas cities. Compare their performance to understand Big O notation.

### Learning Objectives
- Implement linear and binary search in Python
- Measure algorithm performance using the `time` module
- Analyze efficiency using Big O notation
- Work with JSON data and Python file I/O

### Prerequisites
- Read Chapter 1 in "Grokking Algorithms" (pages 3-19)
- Basic programming knowledge (functions, lists, dictionaries)

---

## 2. Algorithm Background

### Linear Search - O(n)
Check each element one by one until found.
```
Best case: O(1) - first element
Worst case: O(n) - last element or not found
```

### Binary Search - O(log n)
Divide sorted list in half repeatedly.
```
Best case: O(1) - middle element
Worst case: O(log n) - requires sorted data
```

### Why It Matters
For 1 million items:
- Linear Search: up to 1,000,000 comparisons
- Binary Search: at most 20 comparisons!

---

## 3. Project Structure

```
lab01_binary_search/
├── search.py      # Search algorithm implementations
├── main.py        # Main program
└── README.md      # Your lab report
```

---

## 4. Step-by-Step Implementation

### Step 1: Create `search.py`

```python
"""
Lab 1: Search Algorithms
Implements linear and binary search for city data.
"""
import time
from typing import Dict, List, Optional


def linear_search(cities: List[Dict], target_name: str) -> Optional[Dict]:
    """
    Perform linear search for a city by name.
    Time Complexity: O(n)
    
    Args:
        cities: List of city dictionaries
        target_name: City name to find
    
    Returns:
        City dict if found, None otherwise
    """
    start_time = time.time()
    comparisons = 0
    
    for city in cities:
        comparisons += 1
        if city['name'].lower() == target_name.lower():
            elapsed = (time.time() - start_time) * 1000
            print(f"Linear Search: Found in {comparisons} comparisons ({elapsed:.4f} ms)")
            return city
    
    elapsed = (time.time() - start_time) * 1000
    print(f"Linear Search: Not found after {comparisons} comparisons ({elapsed:.4f} ms)")
    return None


def binary_search(cities: List[Dict], target_name: str) -> Optional[Dict]:
    """
    Perform binary search for a city by name.
    Time Complexity: O(log n)
    REQUIRES: cities list must be sorted by name!
    
    Args:
        cities: Sorted list of city dictionaries
        target_name: City name to find
    
    Returns:
        City dict if found, None otherwise
    """
    start_time = time.time()
    comparisons = 0
    
    left = 0
    right = len(cities) - 1
    target_lower = target_name.lower()
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        mid_name = cities[mid]['name'].lower()
        
        if mid_name == target_lower:
            elapsed = (time.time() - start_time) * 1000
            print(f"Binary Search: Found in {comparisons} comparisons ({elapsed:.4f} ms)")
            return cities[mid]
        elif mid_name < target_lower:
            left = mid + 1
        else:
            right = mid - 1
    
    elapsed = (time.time() - start_time) * 1000
    print(f"Binary Search: Not found after {comparisons} comparisons ({elapsed:.4f} ms)")
    return None
```

### Step 2: Create `main.py`

```python
"""
Lab 1: Main Program
Demonstrates linear vs binary search on city data.
"""
import json
from search import linear_search, binary_search


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filename}!")
        return []


def main():
    # Load city data
    cities = load_cities('../data/cities.json')
    if not cities:
        return
    
    print(f"Loaded {len(cities)} cities\n")
    print("=" * 50)
    
    # Test city to search for
    test_city = "Plano"
    
    # LINEAR SEARCH (works on unsorted data)
    print(f"\nSearching for '{test_city}' using Linear Search...")
    result = linear_search(cities, test_city)
    if result:
        print(f"  Found: {result['name']}, Population: {result['population']:,}")
    
    # BINARY SEARCH (requires sorted data)
    print(f"\nSorting cities alphabetically...")
    cities_sorted = sorted(cities, key=lambda x: x['name'].lower())
    
    print(f"\nSearching for '{test_city}' using Binary Search...")
    result = binary_search(cities_sorted, test_city)
    if result:
        print(f"  Found: {result['name']}, Population: {result['population']:,}")
    
    # Compare with a city at the end of the alphabet
    print("\n" + "=" * 50)
    test_city2 = "San Antonio"
    
    print(f"\nSearching for '{test_city2}' (near end of sorted list)...")
    print("\nLinear Search:")
    linear_search(cities, test_city2)
    
    print("\nBinary Search:")
    binary_search(cities_sorted, test_city2)
    
    # Test non-existent city
    print("\n" + "=" * 50)
    print("\nSearching for 'Springfield' (doesn't exist)...")
    print("\nLinear Search:")
    linear_search(cities, "Springfield")
    
    print("\nBinary Search:")
    binary_search(cities_sorted, "Springfield")


if __name__ == "__main__":
    main()
```

---

## 5. Expected Output

```
Loaded 20 cities

==================================================

Searching for 'Plano' using Linear Search...
Linear Search: Found in 9 comparisons (0.0234 ms)
  Found: Plano, Population: 287,677

Sorting cities alphabetically...

Searching for 'Plano' using Binary Search...
Binary Search: Found in 4 comparisons (0.0089 ms)
  Found: Plano, Population: 287,677

==================================================

Searching for 'San Antonio' (near end of sorted list)...

Linear Search:
Linear Search: Found in 4 comparisons (0.0156 ms)

Binary Search:
Binary Search: Found in 3 comparisons (0.0067 ms)

==================================================

Searching for 'Springfield' (doesn't exist)...

Linear Search:
Linear Search: Not found after 20 comparisons (0.0312 ms)

Binary Search:
Binary Search: Not found after 5 comparisons (0.0078 ms)
```

---

## 6. Lab Report Template

Create `README.md` in your lab folder:

```markdown
# Lab 1: Binary Search

## Student Information
- **Name:** [Your Name]
- **Date:** [Date]

## Algorithm Summary

### Linear Search
- **How it works:** [Your explanation]
- **Time Complexity:** O(n)
- **Best for:** [When to use]

### Binary Search  
- **How it works:** [Your explanation]
- **Time Complexity:** O(log n)
- **Requirement:** Data must be sorted
- **Best for:** [When to use]

## Test Results

| Search Term | Linear (comparisons) | Binary (comparisons) |
|-------------|---------------------|---------------------|
| Plano       |                     |                     |
| San Antonio |                     |                     |
| Springfield |                     |                     |

## Reflection Questions

1. Why is binary search faster than linear search?

2. What is the tradeoff of using binary search?

3. If you had 1 million cities, approximately how many comparisons would each algorithm need in the worst case?

## Challenges Encountered
[Describe any issues and how you resolved them]
```

---

## 7. Submission

1. Ensure all files are saved in `lab01_binary_search/`
2. Complete your lab README
3. Commit and push to GitHub
4. Continue to Lab 2!
