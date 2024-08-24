
# Text Justification

## Overview

Text Justification is a simple algorithm that aligns text into a justified format, ensuring that each line (except the last) has an equal number of characters (if possible) by adjusting the spacing between words. This project provides a solution for justifying text to a specific width.

## Features

- **Dynamic Line Width:** The program allows you to specify the maximum width for each line.
- **Word Wrapping:** Automatically wraps words to the next line when they exceed the specified width.
- **Even Spacing:** Distributes extra spaces evenly between words to achieve full justification.
- **Edge Cases Handling:** Manages various edge cases like single-word lines, multiple spaces, and very short or very long words.

## Usage

### Input
- **Text:** A list of words to be justified.
- **Width:** An integer specifying the maximum number of characters per line.

### Output
- A list of strings where each string represents a fully justified line of text.

### Example

```python
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

# Output
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

### Implementation

The main steps to achieve text justification are:

1. **Line Building:** 
   - Group words together to form lines that do not exceed the specified width.
2. **Space Distribution:**
   - Calculate the number of spaces needed between words to fully justify the line.
   - Distribute extra spaces from left to right to ensure an even distribution.
3. **Edge Case Handling:**
   - Ensure the last line is left-justified, with no extra spacing between words.
   - Handle cases where a line has only one word.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/text-justification.git
cd text-justification
```

### Running the Code

To run the text justification script:

```bash
python justify_text.py
```

### Testing

To run tests:

```bash
python -m unittest discover tests
```

## Contributing

We welcome contributions! Please fork this repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add Your Feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

