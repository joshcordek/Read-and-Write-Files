import pandas as pd

# Load and read file
sales_csv = 'sales.csv'
df = pd.read_csv(sales_csv)

# Calculate totals
df['Total'] = df['SubTotal'] + df['TaxAmt'] + df['Freight']

# Sum total by ID group
salesreport_df = df.groupby('CustomerID', as_index=False)['Total'].sum()

# Create new File
salesreport_csv = 'salesreport.csv'
salesreport_df.to_csv(salesreport_csv, index=False)

# Display new file
print(salesreport_df.head())
