# Import pandas library for data manipulation and analysis
import pandas as pd
# Import numpy library for numerical computing
import numpy as np

# Print confirmation message
print("PyCharm setup complete!")
# Display the installed version of pandas
print(f"Pandas version: {pd.__version__}")
# Display the installed version of numpy
print(f"NumPy version: {np.__version__}")
print("\nReady to start learning!")

# Import sys module to access system-specific parameters
import sys
# Re-import pandas (duplicate import, already imported above)
import pandas as pd
# Print the path to the Python interpreter being used
print(sys.executable)
# Print pandas version again (duplicate check)
print(pd.__version__)
