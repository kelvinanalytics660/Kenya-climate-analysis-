import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('kenya_climate_data.csv')

# Preview data
print("First 5 rows:")
print(data.head())

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Drop missing values (cleaning)
data = data.dropna()

# Convert date column if exists
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')

# Basic statistics
print("\nSummary statistics:")
print(data.describe())

# Plot 1: Trend over time
if 'Date' in data.columns:
    plt.figure()
   # Improved Plot 1: Trend over time
if 'Date' in data.columns:
    plt.figure(figsize=(10,5))
    plt.plot(data['Date'], data[data.columns[1]])
    plt.title("Climate Trend Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Improved Plot 2: Distribution
plt.figure(figsize=(8,5))
plt.hist(data[data.columns[1]], bins=20)
plt.title("Distribution of Climate Values", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show() (data['Date'], data[data.columns[1]])
    plt.title("Climate Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.show()

# Plot 2: Distribution
plt.figure()
data[data.columns[1]].hist()
plt.title("Distribution of Climate Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
