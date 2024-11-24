# Arrays & Hashing Python Data Structures Study Guide

## Table of Contents
1. [Dynamic Arrays](#dynamic-arrays)
2. [Hash Tables (Dictionaries)](#hash-tables)
3. [Hash Implementation](#hash-implementation)
4. [Prefix Sums](#prefix-sums)
5. [Problem-Solving Patterns](#problem-solving-patterns)
6. [Additional Important Concepts](#additional-concepts)

## Dynamic Arrays

Python lists are implemented as dynamic arrays behind the scenes, providing automatic resizing capabilities.

### When to Use Dynamic Arrays
* When you need sequential storage with fast access by index
* When elements need to be processed in order
* When you frequently append/remove from the end
* When memory locality is important (elements stored contiguously)

### Problem-Solving Indicators
Look for these phrases in problem descriptions:
* "Find the maximum/minimum element"
* "Find the kth element"
* "Process elements in order"
* "Rotate array"
* "Reverse array or parts of array"
* "Sliding window"

### Time Complexities
```python
# Constant Time Operations O(1)
my_dynamic_array.append(element)     # Add to end (amortized O(1))
my_dynamic_array[index]             # Access element by index
my_dynamic_array[index] = element   # Update element at index
my_dynamic_array.pop()              # Remove last element

# Linear Time Operations O(n)
my_dynamic_array.insert(index, element)  # Insert at specific index
my_dynamic_array.pop(index)              # Remove from specific index
my_dynamic_array.remove(element)         # Remove first occurrence of element
element in my_dynamic_array              # Search for element
```

## Hash Tables

Hash tables provide fast key-value storage with constant-time average operations.

### When to Use Hash Tables
* When you need to count frequencies
* When you need to check for existence quickly
* When mapping values to other values
* When detecting duplicates
* When storing/retrieving data by key
* When caching results

### Problem-Solving Indicators
Look for these phrases:
* "Find the first duplicate"
* "Count the number of occurrences"
* "Find two numbers that sum to..."
* "Check if it contains..."
* "Find matching pairs"
* "Track frequency of..."
* "Group items by..."
* Anything involving "unique" elements
* Problems requiring O(1) lookup

### Common Hash Table Patterns

1. Frequency Counter Pattern
```python
def solve_frequency_problem(elements):
    # Common pattern for counting problems
    frequency = {}
    for element in elements:
        frequency[element] = frequency.get(element, 0) + 1
    
    # Now you can:
    # 1. Find most common element
    # 2. Check for duplicates
    # 3. Compare frequencies
    # 4. Find elements with specific frequency
    return frequency
```

2. Two-Sum Pattern
```python
def find_pair_with_sum(numbers, target_sum):
    # Common pattern for pair finding problems
    seen_numbers = {}  # number -> index
    
    for index, number in enumerate(numbers):
        complement = target_sum - number
        if complement in seen_numbers:
            return [seen_numbers[complement], index]
        seen_numbers[number] = index
    return []
```

3. Grouping Pattern
```python
def group_by_property(items):
    # Common pattern for grouping problems
    groups = {}
    for item in items:
        key = some_property(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups
```

## Prefix Sums

### When to Use Prefix Sums
* When dealing with range sum queries
* When you need to calculate running sums
* When finding subarrays with specific sum
* When working with cumulative properties

### Problem-Solving Indicators
Look for these phrases:
* "Find sum of subarray"
* "Calculate sum between indices"
* "Find number of subarrays with sum..."
* "Continuous sequence of numbers that sum to..."
* "Running total"
* "Cumulative sum"

### Common Prefix Sum Patterns

1. Range Query Pattern
```python
def setup_range_queries(numbers):
    # Build prefix sum array
    prefix_sums = [0] * (len(numbers) + 1)
    for i in range(len(numbers)):
        prefix_sums[i + 1] = prefix_sums[i] + numbers[i]
    return prefix_sums

def query_range(prefix_sums, left, right):
    # Get sum of range in O(1)
    return prefix_sums[right + 1] - prefix_sums[left]
```

2. Subarray Sum Pattern
```python
def find_subarray_with_sum(numbers, target):
    # Find subarray that sums to target
    prefix_sum = 0
    seen_sums = {0: -1}  # sum -> index mapping
    
    for i, num in enumerate(numbers):
        prefix_sum += num
        if prefix_sum - target in seen_sums:
            return (seen_sums[prefix_sum - target] + 1, i)
        seen_sums[prefix_sum] = i
    return None
```

## Common Problem Types and Their Solutions

### 1. Finding Pairs
Problem indicators:
* "Find pairs that sum to..."
* "Find two elements that..."
* "Match each element with..."

Solution approach:
```python
def find_pairs(numbers, condition):
    seen = {}  # Use hash table for O(1) lookup
    pairs = []
    
    for num in numbers:
        # Look for matching pair
        if condition(num) in seen:
            pairs.append((num, condition(num)))
        # Store current number
        seen[num] = True
    return pairs
```

### 2. Sliding Window Problems
Problem indicators:
* "Find longest/shortest subarray..."
* "Find maximum/minimum in window of size k"
* "Find continuous sequence..."

Solution approach:
```python
def sliding_window(arr, k):
    window = {}  # or use array for fixed-size window
    left = right = 0
    
    while right < len(arr):
        # Add element to window
        add_to_window(window, arr[right])
        
        # Shrink window if needed
        while window_condition_broken():
            remove_from_window(window, arr[left])
            left += 1
            
        # Update result
        right += 1
```

### 3. Frequency Problems
Problem indicators:
* "Find most common..."
* "Count number of..."
* "Find elements that appear..."

Solution approach:
```python
def solve_frequency(elements):
    # Use Counter for built-in frequency counting
    from collections import Counter
    frequencies = Counter(elements)
    
    # Or manual counting
    frequencies = {}
    for elem in elements:
        frequencies[elem] = frequencies.get(elem, 0) + 1
```

## Best Practices for Problem Solving

1. Initial Analysis:
   * Read problem carefully and identify pattern indicators
   * Consider time/space complexity requirements
   * Look for keywords suggesting specific data structures

2. Solution Selection:
   * Hash Table: When O(1) lookup needed
   * Array: When order matters or need index access
   * Prefix Sum: When dealing with range queries
   * Set: When only need to track existence

3. Implementation Tips:
   * Start with brute force, then optimize
   * Consider edge cases early
   * Use descriptive variable names
   * Add comments for complex logic
   * Test with various scenarios

4. Optimization Considerations:
   * Can you reduce time complexity using a hash table?
   * Would preprocessing (like prefix sums) help?
   * Is there a more space-efficient approach?
   * Can you solve in-place?

Remember: Many problems can be solved with multiple approaches. The key is identifying the most efficient solution based on the problem's constraints and requirements.