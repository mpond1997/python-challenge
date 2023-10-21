import os
import csv
#Define Values
candidate = []
num_votes = []
vote_percent = []
total_votes = 0


election_data_csv = os.path.join('PyPoll','Resources', 'election_data.csv')

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            num_votes.append(1)
        else:
            index = candidate.index(row[2])
            num_votes[index] += 1
    
     
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        vote_percent.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidate[index]

#Printing results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(vote_percent[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Printing in output file
output = open("output", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate)):
    line = str(f"{candidate[i]}: {str(vote_percent[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))   