import csv

file_path = 'employee_data.csv'

with open(file_path, 'r') as file:
    employee_data_reader = csv.reader(file)
    headers = next(employee_data_reader)
    
    for row in employee_data_reader:
        for header, value in zip(headers, row):
            print(f"{header}: {value}")
        print("")
