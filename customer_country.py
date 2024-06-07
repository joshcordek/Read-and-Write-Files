import pandas as pd

#Load and read file
customer_csv = 'customers.csv'
df = pd.read_csv(customer_csv)

#Display file
df.head()

#Create new file
new_df = df[['LastName','FirstName', 'Country']].copy()
new_df['CustomerName'] = new_df['LastName'] + ', ' + new_df['FirstName']
new_df = new_df[['CustomerName', 'Country']]

country_csv = 'customer_country.csv'
new_df.to_csv(country_csv, index=False)

#Display new file
new_df.head()
