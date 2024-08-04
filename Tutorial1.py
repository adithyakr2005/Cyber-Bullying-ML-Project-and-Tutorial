import pandas as pd

file_path = r'C:\Users\adith\Downloads\archive\smartphone-cleaned.csv'

try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    
print("First few rows of the dataset:")
print(data.head())
    
print("\nSummary statistics:")
print(data.describe())
    
print("\nData types of each column:")
print(data.dtypes)

