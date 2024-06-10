import csv

sales_csv = 'sales.csv'
salesreport_csv = 'salesreport.csv'
customer_totals = {}

with open(sales_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        customer_id = row[0]
        total = float(row[3])
        if customer_id in customer_totals:
            customer_totals[customer_id] += total
        else:
            customer_totals[customer_id] = total

with open(salesreport_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['CustomerID', 'Total'])
    for customer_id, total in customer_totals.items():
        csvwriter.writerow([customer_id, total])
