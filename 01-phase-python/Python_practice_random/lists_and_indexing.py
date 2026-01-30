# Create a list of personal goals
goals = ["health","career progression", "Financial Stability", "Family", "Self-Discipline"]

# Access list elements using different indexing methods
print("First", goals[0])              # Access first element using index 0
print("Last", goals[-1])               # Access last element using negative indexing
print("Middle:",goals[len(goals)//2])  # Access middle element by calculating index (length//2)

# Modify an existing list element by index
goals[1] = "Breaking into Data Engineering"  # Replace second element

# Add a new element to the end of the list
goals.append("long-term wealth")

# Print the updated list
print("\nUpdated Goals", goals)
