import os
import csv

election_data_csv = os.path.join('..','resources', 'election_data.csv')

with open(election_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)