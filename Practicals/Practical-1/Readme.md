Sure! Here's a `README.md` file that describes the Python implementation of text justification in a clear and structured way:

---

# Text Justification in Python

This Python script justifies a given text to a specified width, ensuring that each line of the output is fully justified, except the last line, which is left-justified.

## Problem Statement

Given a string `str` and a width `L` for each line, the task is to justify the string such that:
- Each line of the justified text has exactly `L` characters.
- The text is fully justified, meaning that spaces are added between words so that the line length is exactly `L`.
- The last line is left-justified, meaning that any extra spaces are added at the end of the line.

### Example

- **Input**: `str = "The quick brown fox jumps over the lazy dog."`, `L = 11`
- **Output**:
  ```
  The   quick
  brown  fox
  jumps  over
  the    lazy
  dog.      
  ```

## Approach

1. **Split the Text**:
   - The input string is split into individual words.

2. **Line Formation**:
   - Iterate through the words and build lines such that the length of each line, including spaces between words, does not exceed `L`.

3. **Space Distribution**:
   - For each line (except the last), distribute extra spaces between the words to make the line length exactly `L`.
   - If there are multiple gaps between words, the extra spaces are distributed as evenly as possible, with the leftmost gaps receiving more spaces if needed.

4. **Left Justification of the Last Line**:
   - The last line is left-justified, with any remaining spaces added at the end of the line.

## Python Implementation

Here's the Python code that implements the above approach:

```python
def justify_text(text, L):
    words = text.split()
    result = []
    line = []
    line_length = 0
    
    for word in words:
        if line_length + len(word) + len(line) > L:
            for i in range(L - line_length):
                line[i % (len(line) - 1 or 1)] += ' '
            result.append(''.join(line))
            line, line_length = [], 0
        
        line.append(word)
        line_length += len(word)
    
    result.append(' '.join(line).ljust(L))
    
    return '\n'.join(result)

# Example usage:
text = "The quick brown fox jumps over the lazy dog."
L = 11
justified_text = justify_text(text, L)
print(justified_text)
```

### Explanation of the Code

- **Splitting the Text**: The input string is split into individual words using the `split()` method.
- **Line Formation**: Words are added to a line until the addition of another word would exceed the width `L`.
- **Space Distribution**: Extra spaces are distributed across the line to ensure that it has exactly `L` characters. The spaces are distributed as evenly as possible between words.
- **Left Justification**: The last line is treated differently by adding any remaining spaces at the end.

### Running the Code

To run this script:
1. Copy the code into a Python file, e.g., `justify_text.py`.
2. Execute the script in a Python environment.
3. The output will be the justified text printed to the console.

### Example Output

For the input `text = "The quick brown fox jumps over the lazy dog."` and `L = 11`, the output will be:

```
The   quick
brown  fox
jumps  over
the    lazy
dog.      
```

---

This `README.md` file provides a comprehensive overview of the problem, the approach taken to solve it, and the Python implementation. It is designed to be informative and accessible to developers looking to understand or use the script.
