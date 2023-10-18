import os
import csv


election_data_csv = os.path.join('..','Resources', 'election_data.csv')

with open(election_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
