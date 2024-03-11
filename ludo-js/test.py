import pandas as pd
import csv

file_path = "C:/Users/kopan/OneDrive/Desktop/shankar_near.csv"

def import_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if present
        for row in csv_reader:
            data.append(row)
    return data

# Import the CSV data
csv_data = import_csv_data(file_path)

# Create a pandas DataFrame from the CSV data
df = pd.DataFrame(csv_data, columns=['Date', 'Currency', 'Type', 'Coin', 'Price', 'Fees', 'Total'])

# Convert the numeric columns to appropriate data types
numeric_columns = ['Coin', 'Price', 'Fees', 'Total']
df[numeric_columns] = df[numeric_columns].astype(float)

# Convert the Date column to a datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Create a pivot table with the necessary columns
pivot_table = df.pivot_table(
    index=['Currency', 'Type'],
    values=['Coin', 'Total', 'Fees', 'Price'],
    aggfunc={'Coin': 'sum', 'Total': 'sum', 'Fees': 'sum', 'Price': 'mean'}
)

# Print the pivot table
print("Pivot Table:")
print(pivot_table)