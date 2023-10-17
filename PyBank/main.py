import os
import csv

budget_data_csv = os.path.join('..', 'resources', 'budget_data.csv')

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for row in csvreader:
        print(row)


