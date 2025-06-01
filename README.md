# Python Sorting Algorithms

This repository contains implementations of common sorting algorithms in Python. Each algorithm is implemented as a function with clear comments explaining the logic. The code is designed for educational purposes, demonstrating how these algorithms work and their performance characteristics.

## Table of Contents
- [Algorithms Included](#algorithms-included)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Algorithm Details](#algorithm-details)
- [Notes](#notes)
- [License](#license)

## Algorithms Included
The following sorting algorithms are implemented:
- **Bubble Sort**: Repeatedly compares and swaps adjacent elements (O(n²)).
- **Selection Sort**: Repeatedly selects the smallest element from the unsorted portion (O(n²)).
- **Insertion Sort**: Builds the sorted list one element at a time (O(n²)).
- **Merge Sort**: Divides and merges sorted sublists (O(n log n)).
- **Quick Sort**: Partitions around a pivot and recursively sorts (O(n log n) average).
- **Heap Sort**: Uses a max-heap to sort elements (O(n log n)).
- **Timsort**: Python’s built-in hybrid sort (O(n log n), optimized for real-world data).
- **Counting Sort**: Counts occurrences for small integer ranges (O(n + k)).
- **Radix Sort**: Sorts by processing digits (O(nk)).
- **Bucket Sort**: Distributes elements into buckets and sorts them (O(n + k) average).

## Requirements
- Python 3.6 or higher
- Optional (for formatting and linting): `black`, `flake8`
- Optional (for testing): `unittest` (included in Python standard library)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-sorting-algorithms.git
   cd python-sorting-algorithms


(Optional) Install formatting/linting tools:pip install black flake8



Usage

Single File: If using sorting_algorithms.py, run:
python3 sorting_algorithms.py

 This executes the test cases included in the file, sorting the array [64, 34, 25, 12, 22, 11, 90] (and [0.64, 0.34, 0.25, 0.12, 0.22, 0.11, 0.90] for bucket sort).

Separate Files: If using individual files, run main.py to test all algorithms:
python3 main.py

 Alternatively, run individual files, e.g.:
python3 bubble_sort.py


Custom Input: Modify the test array in sorting_algorithms.py or main.py to sort custom data. Example:
test_arr = [your, custom, array]
print(bubble_sort(test_arr.copy()))



Running Tests
Unit tests are provided in tests/test_sorting.py. Run them with:
python3 -m unittest tests/test_sorting.py

This verifies that each algorithm correctly sorts the test array.
Algorithm Details



k: Range of input values (Counting Sort) or number of digits (Radix Sort).
Stability: A stable sort preserves the relative order of equal elements.

Notes

Input Assumptions:
Counting Sort and Radix Sort assume non-negative integers. For negative numbers, preprocess by shifting values.
Bucket Sort assumes inputs in [0, 1). Normalize data if needed (e.g., divide by max value).


Quick Sort: Call with quick_sort(arr, 0, len(arr)-1) for the full array.
Timsort: Uses Python’s built-in sorted() function, as implementing Timsort from scratch is complex.
Performance: For large datasets, Timsort, Merge Sort, or Quick Sort are recommended. Use Counting/Radix Sort for specific integer ranges and Bucket Sort for uniform distributions.
Testing: The included test array is small for demonstration. For performance testing, use larger arrays (e.g., [64, 34, 25, 12, 22, 11, 90] * 100).

