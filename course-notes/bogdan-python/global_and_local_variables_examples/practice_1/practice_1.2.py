# Import the entire practice_1 module
import practice_1
# Import only the mult function directly from practice_1
from practice_1 import mult

# Access the global variable 'c' from practice_1 module using dot notation
print(practice_1.c)  # Output: True
# Call the imported mult function directly (no module prefix needed)
print(mult(100,20))  # Output: 2000

