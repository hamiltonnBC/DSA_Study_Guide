

"""
Essential Python Methods for Array/Hashing LeetCode Problems
Focus: Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams,
      Top K Frequent Elements, Product of Array Except Self,
      Longest Consecutive Sequence
"""

# ---------- ARRAY METHODS ----------

# enumerate() - Returns index and value pairs from an iterable
# Consider when you need both the index and value while iterating
nums = [10, 20, 30]
for i, num in enumerate(nums):
   print(f"Index: {i}, Value: {num}")  # Index: 0, Value: 10 etc.

# range() - Generates a sequence of numbers
# Use when you need to iterate using indices
for i in range(len(nums)):  # 0, 1, 2
   print(nums[i])

# zip() - Combines multiple iterables into tuples
# Perfect for when you need to iterate through multiple lists simultaneously
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
   print(num, letter)  # 1 'a', 2 'b', 3 'c'

# sorted() - Returns a new sorted list
# Use when you need elements in order but want to keep original list unchanged
nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)  # [1, 1, 3, 4, 5]

# ---------- DICTIONARY METHODS ----------

# dict.get() - Safely retrieves value from dictionary with default
# Use instead of direct access to avoid KeyError
counts = {'a': 1, 'b': 2}
value = counts.get('c', 0)  # Returns 0 if 'c' not found

# dict.setdefault() - Sets default value if key doesn't exist
# Useful for initializing values in a dictionary
counts = {}
counts.setdefault('a', 0)  # Creates key 'a' with value 0 if not exists
counts['a'] += 1  # Safe to increment now

# Counter from collections - Creates frequency dictionary
# Perfect for counting elements or characters
from collections import Counter
nums = [1, 1, 2, 2, 2, 3]
counts = Counter(nums)  # {2: 3, 1: 2, 3: 1}

# defaultdict from collections - Dictionary with default factory
# Use when you need a dictionary that can initialize values automatically
from collections import defaultdict
grouped = defaultdict(list)  # Default value is empty list
grouped['a'].append(1)  # No need to check if 'a' exists first

# ---------- SET METHODS ----------

# set() - Creates collection of unique elements
# Use when you need to eliminate duplicates or check existence quickly
unique_nums = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# set operations (intersection, union, difference)
# Useful for finding common or unique elements between collections
set1 = {1, 2, 3}
set2 = {2, 3, 4}
common = set1 & set2  # Intersection: {2, 3}
all_nums = set1 | set2  # Union: {1, 2, 3, 4}
unique_to_set1 = set1 - set2  # Difference: {1}

# ---------- STRING METHODS ----------

# str.join() - Combines list elements into string
# Use when you need to create string from list of characters
chars = ['h', 'e', 'l', 'l', 'o']
word = ''.join(chars)  # 'hello'

# str.split() - Splits string into list
# Use when you need to break string into components
sentence = "hello world"
words = sentence.split()  # ['hello', 'world']

# ---------- OTHER USEFUL TOOLS ----------

# max() and min() - Find extreme values
# Use when you need largest/smallest element or comparison result
nums = [1, 5, 3, 2, 4]
largest = max(nums)  # 5
smallest = min(nums)  # 1

# list slicing - Get portion of list
# Use for getting subsets of lists
nums = [0, 1, 2, 3, 4]
subset = nums[1:4]  # [1, 2, 3]

# list comprehension - Create lists concisely
# Use for transforming elements or filtering
nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]  # [1, 4, 9, 16, 25]
evens = [x for x in nums if x % 2 == 0]  # [2, 4]

# ---------- TIME COMPLEXITY TIPS ----------
"""
Common operations and their time complexities:
- List index/append/pop at end: O(1)
- List insert/delete at beginning/middle: O(n)
- Dictionary/Set add/remove/lookup: O(1) average
- Sorting: O(n log n)
- Linear search: O(n)
- Binary search (on sorted list): O(log n)
"""

############################################################################################################

# DICTIONARIES
print("-------- DICTIONARY OPERATIONS --------")

# Create empty dictionary
my_dict = {}

# Adding key-value pairs - three equivalent ways:
my_dict['name'] = 'John'           # Method 1
my_dict.update({'age': 25})        # Method 2
my_dict.update(city='New York')    # Method 3

print("Dictionary after adding items:", my_dict)
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}

# Get value by key - different methods:
name = my_dict['name']              # Method 1 - will raise KeyError if key doesn't exist
age = my_dict.get('age')           # Method 2 - returns None if key doesn't exist
city = my_dict.get('city', 'Unknown')  # Method 3 - returns 'Unknown' if key doesn't exist

print("\nRetrieving values:")
print("Name:", name)
print("Age:", age)
print("City:", city)

# Get all values
all_values = my_dict.values()
print("\nAll values:", all_values)

# Get all keys
all_keys = my_dict.keys()
print("All keys:", all_keys)

# Check if key exists
if 'name' in my_dict:
   print("\nName exists in dictionary!")

# Iterate over both keys and values
print("\nIterating over dictionary:")
for key, value in my_dict.items():
   print(f"Key: {key}, Value: {value}")

# Dictionary Gotchas and Tips
print("\nDictionary Gotchas and Tips:")
# If you try to access a non-existent key:
try:
   phone = my_dict['phone']  # Will raise KeyError
except KeyError:
   print("KeyError avoided using try-except!")

# Better to use .get() to avoid errors:
phone = my_dict.get('phone')  # Returns None
phone_with_default = my_dict.get('phone', 'Not Found')
print("Getting non-existent key with .get():", phone)
print("Getting non-existent key with default:", phone_with_default)

# Update multiple key-value pairs at once:
my_dict.update({
   'phone': '123-456-7890',
   'email': 'john@example.com'
})
print("\nDictionary after updating multiple pairs:", my_dict)

# SETS
print("\n\n-------- SET OPERATIONS --------")

# Create empty set
my_set = set()      # Must use set() - my_set = {} creates a dictionary!

# Create set with initial values
my_set = {1, 2, 3}
print("Initial set:", my_set)

# Adding elements
my_set.add(4)           # Add single element
my_set.update([5, 6])   # Add multiple elements
my_set.update({7, 8}, {9, 10})  # Can add multiple sets at once

print("Set after adding elements:", my_set)

# Set Operations demonstration
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet Operations with set1:", set1, "and set2:", set2)

# Union (all elements from both sets)
union = set1 | set2  # or set1.union(set2)
print("Union:", union)

# Intersection (elements common to both sets)
intersection = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection)

# Difference (elements in set1 but not in set2)
difference = set1 - set2  # or set1.difference(set2)
print("Difference (set1 - set2):", difference)

# Symmetric Difference (elements in either set but not both)
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)

# Removing Elements demonstration
my_set = {1, 2, 3, 4, 5}
print("\nDemonstrating removal from set:", my_set)

my_set.remove(1)     # Raises KeyError if element not found
print("After removing 1:", my_set)

my_set.discard(2)    # Won't raise error if element not found
print("After discarding 2:", my_set)

popped = my_set.pop()  # Removes and returns arbitrary element
print("After popping an element:", my_set, "(Popped value:", popped, ")")

# Membership and Other Operations
print("\nMembership and Other Operations:")
my_set = {1, 2, 3, 4}
print("Checking if 1 exists in", my_set, ":", 1 in my_set)
print("Checking if 5 exists in", my_set, ":", 5 in my_set)

# Subset/Superset checks
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("\nChecking if", set1, "is subset of", set2, ":", set1.issubset(set2))
print("Checking if", set2, "is superset of", set1, ":", set2.issuperset(set1))

# Common Use Cases
print("\nCommon Set Use Cases:")
# Remove duplicates from a list
my_list = [1, 2, 2, 3, 3, 4]
unique_list = list(set(my_list))
print("Removing duplicates from", my_list, ":", unique_list)

# Find unique characters in string
text = "hello"
unique_chars = set(text)
print("Unique characters in", text, ":", unique_chars)

# Check if two lists have common elements
list1 = [1, 2, 3]
list2 = [3, 4, 5]
common = set(list1) & set(list2)
print("Common elements between", list1, "and", list2, ":", common)