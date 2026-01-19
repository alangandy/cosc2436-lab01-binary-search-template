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

## Your Tasks

### Task 1: Implement `linear_search()`
Complete the `linear_search()` function in `search.py`:
- Loop through each item in the list
- Count each comparison
- Return the item and comparison count when found
- Return `(None, comparisons)` if not found

### Task 2: Implement `binary_search()`
Complete the `binary_search()` function in `search.py`:
- Use `left` and `right` pointers to track the search range
- Calculate the middle index: `mid = (left + right) // 2`
- Compare and adjust pointers accordingly
- Count each comparison
- Return the item and comparison count

## Example

```python
# For a list of 1000 cities:
# Linear search: up to 1000 comparisons
# Binary search: at most 10 comparisons (log₂(1000) ≈ 10)
```

## Testing
Run the tests to verify your implementation:
```bash
python -m pytest tests/ -v
```

## Hints
- Remember: Binary search requires sorted data!
- Use `.lower()` for case-insensitive comparison
- The comparison count helps you see the efficiency difference

## Submission
Commit and push your completed `search.py` file.
