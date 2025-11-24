# Phase 1: Python Fundamentals - Learning Notes

**Duration:** Weeks 1-4 (Month 1)
**Status:** Not Started

---

## Key Concepts

### Core Python Fundamentals
- Variables and data types
- Control flow (if/else, loops)
- Functions and scope
- Error handling (try/except)
- File I/O operations

### Data Structures
- Lists, tuples, sets, dictionaries
- List comprehensions
- Dictionary operations
- When to use which data structure

### Object-Oriented Programming
- Classes and objects
- Inheritance and polymorphism
- Magic methods
- Encapsulation

### Working with Data
- Reading/writing CSV and JSON files
- Data manipulation with Pandas
- NumPy basics for numerical operations
- Basic data cleaning techniques

---

## Code Patterns

### File Reading Pattern
```python
# CSV reading with Pandas
import pandas as pd

df = pd.read_csv('data.csv')
# Process data
df_cleaned = df.dropna()
df_cleaned.to_csv('output.csv', index=False)
```

### Error Handling Pattern
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error()
finally:
    cleanup()
```

### Function Documentation Pattern
```python
def process_data(input_file: str, output_file: str) -> bool:
    """
    Process data from input file and save to output file.

    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file

    Returns:
        bool: True if successful, False otherwise
    """
    # Implementation
    pass
```

---

## Resources Used

### Primary Course
- [Bogdan Python Course - add link]
- Progress: 0%

### Supplementary Resources
- Python official documentation: https://docs.python.org/3/
- Real Python tutorials: https://realpython.com/
- Pandas documentation: https://pandas.pydata.org/docs/

### Practice Platforms
- LeetCode (Python problems)
- HackerRank (Python track)
- Project Euler (mathematical problems)

---

## Personal Notes

### Week 1
[Add your notes about what you learned]

### Week 2
[Add your notes about what you learned]

### Week 3
[Add your notes about what you learned]

### Week 4
[Add your notes about what you learned]

---

## Key Takeaways

[Add your main learnings from this phase]

---

## Questions / Areas for Review

[Note any concepts that need more practice or clarification]

---

## Practical Applications

[Note how these concepts apply to data engineering work]
