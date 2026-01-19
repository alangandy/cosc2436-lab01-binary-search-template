# Lab 01: Binary Search

## Overview
Implement linear search and binary search algorithms to understand Big O notation and algorithm efficiency.

## Learning Objectives
- Implement linear search O(n) and binary search O(log n)
- Understand Big O notation
- Compare algorithm performance

## Files to Complete
- `search.py` - Implement `linear_search()` and `binary_search()` functions
- `README.md` - Complete the lab report section below

## Instructions

### Part 1: Implement Linear Search
Complete the `linear_search()` function in `search.py`:
- Search through the list one element at a time
- Return the item if found, None otherwise
- Track the number of comparisons made

### Part 2: Implement Binary Search
Complete the `binary_search()` function in `search.py`:
- The input list must be sorted
- Use divide and conquer: check middle, eliminate half
- Return the item if found, None otherwise

### Part 3: Run Tests
```bash
python -m pytest tests/ -v
```

### Part 4: Complete Lab Report
Fill in the sections below.

---

## Lab Report

### Student Information
- **Name:** [Your Name]
- **Date:** [Date]

### Algorithm Analysis

#### Linear Search
- **Time Complexity:** O(?)
- **How it works:** [Your explanation]

#### Binary Search
- **Time Complexity:** O(?)
- **How it works:** [Your explanation]
- **Requirement:** [What must be true about the data?]

### Test Results

| Search Term | Linear (comparisons) | Binary (comparisons) |
|-------------|---------------------|---------------------|
| Houston     |                     |                     |
| Plano       |                     |                     |
| Nonexistent |                     |                     |

### Reflection Questions

1. Why is binary search faster than linear search?

   [Your answer]

2. What is the tradeoff of using binary search?

   [Your answer]

3. If you had 1 million items, how many comparisons would each algorithm need in the worst case?

   [Your answer]

### Challenges Encountered
[Describe any issues and how you resolved them]
