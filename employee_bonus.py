import pandas as pd

# Load the file
file_path = 'employee_data.csv'
employee_df = pd.read_csv(file_path)

# Display data
for index, row in employee_df.iterrows():
    print('Employee ID:', row['ID'])
    print('Name:', row['Name'])
    print('Age:', row['Age'])
    print('Salary:', row['Salary'])
    print('Hours:', row['HoursWorked'])
    print('Productivity:', row['Productivity'])
    print('Team:', row['Team'])
    print('Bonus:', row['Bonus'])
    print("")
