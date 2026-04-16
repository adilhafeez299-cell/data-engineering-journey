# Define a global variable 'c' with boolean value
c = True

def mult(a, b):
    # Create a LOCAL variable 'c' inside the function
    # This is a different variable from the global 'c' (variable shadowing)
    c = a * b
    # Return the local 'c' value
    return c

# Call mult function - uses and returns the local 'c' inside the function
print(mult(100,30))  # Output: 3000 (local c = 100 * 30)
# Print the global 'c' - unchanged because the function created its own local 'c'
print(c)  # Output: True (global c remains unchanged)