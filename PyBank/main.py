import os
import csv

csvpath = os.path.join('PyBank','resources', 'budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    row_count = sum(1 for row in csvreader)
    Total_Months = row_count
    print(Total_Months)

output_path = os.path.join('PyBank','Analysis','Output')

with open(output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(['Total Months: '])
    csvwriter.writerow(['Total: '])
    csvwriter.writerow(['Average Change: '])
    csvwriter.writerow(['Greatest Increase in Profits: '])
    csvwriter.writerow(['Greatest Decrease in Profits: '])



    
    
    
