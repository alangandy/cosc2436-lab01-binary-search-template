"""
Lab 01: Main Program
Demonstrates linear vs binary search on city data.
"""
import json
from search import linear_search, binary_search


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # Load city data
    cities = load_cities('data/cities.json')
    print(f"Loaded {len(cities)} cities\n")
    
    # Sort cities for binary search
    cities_sorted = sorted(cities, key=lambda x: x['name'].lower())
    
    # Test searches
    test_names = ["Houston", "Plano", "Springfield"]
    
    print("=" * 60)
    print("SEARCH COMPARISON")
    print("=" * 60)
    
    for name in test_names:
        print(f"\nSearching for '{name}':")
        print("-" * 40)
        
        # Linear search
        result, comparisons = linear_search(cities, name)
        if result:
            print(f"Linear Search: Found in {comparisons} comparisons")
            print(f"  → {result['name']}, Pop: {result['population']:,}")
        else:
            print(f"Linear Search: Not found ({comparisons} comparisons)")
        
        # Binary search
        result, comparisons = binary_search(cities_sorted, name)
        if result:
            print(f"Binary Search: Found in {comparisons} comparisons")
            print(f"  → {result['name']}, Pop: {result['population']:,}")
        else:
            print(f"Binary Search: Not found ({comparisons} comparisons)")
    
    # Summary
    print("\n" + "=" * 60)
    print("BIG O SUMMARY")
    print("=" * 60)
    print(f"""
    For {len(cities)} cities:
    - Linear Search worst case: {len(cities)} comparisons
    - Binary Search worst case: ~{len(cities).bit_length()} comparisons
    
    For 1,000,000 items:
    - Linear Search: up to 1,000,000 comparisons
    - Binary Search: up to 20 comparisons (log₂ 1,000,000 ≈ 20)
    """)


if __name__ == "__main__":
    main()
