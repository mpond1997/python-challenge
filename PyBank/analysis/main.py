import os
import csv
# File Location
csvpath = os.path.join('PyBank','resources', 'budget_data.csv')
# Defining Values
total = 0
value = 0
avg_change = 0
date = []
profits = []
# Opening csvfile and printing header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Header row
    csv_header = next(csvreader)
    
    first_row = next(csvreader)
    total += int(first_row[1])
    value = int(first_row[1])
    for row in csvreader:
        date.append(row[0])
        
        change = int(row[1])-value
        profits.append(change)
        value - int(row[1])
# Calculating rows for months
        total_months = sum(1 for row in csvreader)
# Calculating sum of Profit/Losses for Total $        
        total = total +int(row[1])



# Calculating Greatest increase and Decrease
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = date[greatest_index]

    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = date[worst_index]

    # Calculating average change
    avg_change =sum(profits)/len(profits)


#Printing values
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


# Writing out info to file (Output)
output = open('PyBank/analysis/Output','w')


line1 = 'Financial Analysis'
line2 = '------------------------'
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f'Total: ${str(total)}')
line5 = str(f'Average Change: ${str(round(avg_change,2))}')
line6 = str(f'Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})')
line7 = str(f'Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))


    
    
    
