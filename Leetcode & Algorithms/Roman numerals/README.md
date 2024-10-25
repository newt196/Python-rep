# Roman to Integer Converter

This Python application converts Roman numeral strings to their integer equivalents. The solution implements efficient rules for Roman numeral addition and subtraction to deliver the correct integer.

## Problem Description

Given a Roman numeral as a string, the goal is to convert it into an integer. Roman numerals use the following symbols and values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

### Rules:
1. If a smaller numeral appears before a larger numeral, it should be subtracted (e.g., `IV` is `4`).
2. Otherwise, numerals are added directly.

## How It Works

The program processes Roman numeral strings in reverse, applying subtraction or addition as needed based on the numeral order.

## Code Overview

### `Solution` Class

The main function, `romanToInt`, in the `Solution` class converts a Roman numeral string to an integer by following these steps:
1. Initialize a dictionary with Roman numeral mappings.
2. Use a `for` loop to traverse the numeral string in reverse.
3. Apply addition or subtraction rules based on numeral values.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_to_int[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total


<img width="574" alt="image" src="https://github.com/user-attachments/assets/9e2a71c8-a281-45d5-8af1-34031bd4e33e">


v<img width="938" alt="image" src="https://github.com/user-attachments/assets/4f97fc0d-1538-49cf-b72a-3ea8c3e95b27">


<img width="572" alt="image" src="https://github.com/user-attachments/assets/5bec5fe6-b586-4915-8686-d70e8bddc003">
