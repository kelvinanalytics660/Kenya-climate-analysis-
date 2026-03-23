import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('kenya_climate_data.csv')

# Show first 5 rows
print(data.head())

# Basic info
print(data.info())

# Plot (example - adjust column names if needed)
data.plot(x=data.columns[0], y=data.columns[1], kind='line')

plt.title("Climate Trend Analysis")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
