import csv

customers = 'customers.csv'
customer_country = 'customer_country.csv'

with open(customers, 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = ['Last Name', 'First Name', 'Country']
    
    with open(customer_country,'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            last_name = row['LastName']
            first_name = row['FirstName']
            country = row['Country']
            writer.writerow({'Last Name': last_name, 'First Name': first_name,  'Country': country})
