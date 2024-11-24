# LeetCode Problem Examples for Array & Hashing Patterns

## Dynamic Arrays Examples

### 1. Two Pointer / Array Manipulation
**LeetCode 189: Rotate Array**
```python
def rotate(nums: List[int], k: int) -> None:
    """
    Given array [1,2,3,4,5,6,7] and k = 3, rotate to [5,6,7,1,2,3,4]
    Pattern: Array manipulation requiring in-place operations
    """
    k = k % len(nums)  # Handle k > len(nums)
    # Reverse entire array
    nums.reverse()
    # Reverse first k elements
    nums[:k] = nums[:k][::-1]
    # Reverse remaining elements
    nums[k:] = nums[k:][::-1]
```

### 2. Sliding Window
**LeetCode 121: Best Time to Buy and Sell Stock**
```python
def maxProfit(prices: List[int]) -> int:
    """
    Pattern: Track minimum while iterating through array
    Input: [7,1,5,3,6,4]
    Output: 5 (buy at 1, sell at 6)
    """
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
```

## Hash Table Examples

### 1. Frequency Counter
**LeetCode 242: Valid Anagram**
```python
def isAnagram(s: str, t: str) -> bool:
    """
    Pattern: Count frequencies and compare
    Input: s = "anagram", t = "nagaram"
    Output: true
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count frequencies in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrease frequencies from second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0
```

### 2. Two Sum Pattern
**LeetCode 1: Two Sum**
```python
def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Pattern: Hash map to store complements
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []
```

### 3. Grouping Pattern
**LeetCode 49: Group Anagrams**
```python
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Pattern: Use hashable key to group similar items
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    groups = {}
    
    for s in strs:
        # Sort string to create key for anagrams
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    
    return list(groups.values())
```

## Prefix Sum Examples

### 1. Range Sum Query
**LeetCode 303: Range Sum Query - Immutable**
```python
class NumArray:
    """
    Pattern: Precompute cumulative sums for O(1) range queries
    Input: nums = [-2, 0, 3, -5, 2, -1]
    Query: sumRange(0, 2) -> 1
    """
    def __init__(self, nums: List[int]):
        self.prefix = [0]  # Include 0 for easier calculations
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
```

### 2. Subarray Sum
**LeetCode 560: Subarray Sum Equals K**
```python
def subarraySum(nums: List[int], k: int) -> int:
    """
    Pattern: Use prefix sum with hash map to find subarrays
    Input: nums = [1,1,1], k = 2
    Output: 2 (subarrays [1,1] occurring at index pairs (0,1) and (1,2))
    """
    count = 0
    curr_sum = 0
    sum_count = {0: 1}  # prefix_sum -> frequency
    
    for num in nums:
        curr_sum += num
        # If curr_sum - k exists in map, we found a valid subarray
        if curr_sum - k in sum_count:
            count += sum_count[curr_sum - k]
        sum_count[curr_sum] = sum_count.get(curr_sum, 0) + 1
    
    return count
```

## Other Common Patterns

### 1. Set Operations
**LeetCode 217: Contains Duplicate**
```python
def containsDuplicate(nums: List[int]) -> bool:
    """
    Pattern: Use set to track seen elements
    Input: [1,2,3,1]
    Output: true
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
```

### 2. Combined Pattern (Hash + Array)
**LeetCode 128: Longest Consecutive Sequence**
```python
def longestConsecutive(nums: List[int]) -> int:
    """
    Pattern: Use set for O(1) lookup while checking sequences
    Input: [100,4,200,1,3,2]
    Output: 4 ([1,2,3,4])
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only check sequences from their smallest number
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length
```

For each of these problems, look for these key indicators in the problem description:

1. **Need tracking/counting?** → Hash Table/Dictionary
2. **Need to find pairs/matches?** → Hash Table + Two Pointer
3. **Range queries?** → Prefix Sum
4. **Order matters?** → Array/List
5. **Need unique elements?** → Set
6. **Subsequence/subarray sum?** → Prefix Sum + Hash Table
7. **Fixed window operations?** → Sliding Window
8. **Need to group similar items?** → Hash Table with appropriate key

Remember to always consider:
- Time complexity requirements
- Space complexity constraints
- Whether you need to modify input in-place
- Edge cases (empty input, single element, duplicates)
- Input size (might affect choice of solution)