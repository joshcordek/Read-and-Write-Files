import csv

input_file = 'customers.csv'
output_file = 'customer_country.csv'

with open(input_file, 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = ['Last Name', 'First Name', 'Country']
    
    with open(output_file,'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            last_name = row['LastName']
            first_name = row['FirstName']
            country = row['Country']
            writer.writerow({'Last Name': last_name, 'First Name': first_name,  'Country': country})
