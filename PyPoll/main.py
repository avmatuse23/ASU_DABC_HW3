# Alena Matusevich    10/08/2023
# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
 
import os
import csv

# A set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join('Resources', 'election_data.csv')
# Set var for the total number of votes cast
total_votes = 0
# Set a dicdtionary to hold candidates names and number of votes for each candidate
candidates_dict = {}
# Set var for winnner of the elections
winner = ""
# Lists to store an elections data
candidates_list = []
total_votes_per_candidate_list = []
percentage_votes_per_candidate_list = []

# Read in the CSV file to add candidates (KEY) to a dictionary and initilize value as an int
with open(budget_data_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    header = next(csvreader)
    
    # Loop through a set of poll data to add candidate names to a dictionary
    for row in csvreader:
        candidates_dict[row[2]] = 0
        total_votes += 1
# Done working with CSV file --> Candidates (KEY) are addeded to Dict

# Read in the CSV file to count votes per candidate (VALUE) and add it to a dictionary
with open(budget_data_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    header = next(csvreader)

    # Loop through a set of poll data to sum up the total number of votes each candidate won (VALUE) and add it to Dict
    for row in csvreader:
        candidates_dict[row[2]] += 1
# Done working with CSV file --> Votes per candidate (Value) are addeded to Dict

# Loop through a dict to fill in the election results lists and to determine an election winner
temp_count = 0 # used in if statment inside the loop 
for key, value in candidates_dict.items():
    # Fill in an election results lists
    candidates_list.append(key)
    total_votes_per_candidate_list.append(value)
    percentage_votes_per_candidate_list.append(round(value*100/total_votes, 3))
   
    # Determine an election winner
    if value > temp_count:
        temp_count = value
        winner = key
# Done with an election data analysis 

#  Format output strings
output1 = "\nElection Results\n"
output_dash = "-------------------------\n"
output2 = f"Total Votes: {str(total_votes)}\n"
output3 = f"{candidates_list[0]}: {str(percentage_votes_per_candidate_list[0])}% ({str(total_votes_per_candidate_list[0])})\n"
output4 = f"{candidates_list[1]}: {str(percentage_votes_per_candidate_list[1])}% ({str(total_votes_per_candidate_list[1])})\n"
output5 = f"{candidates_list[2]}: {str(percentage_votes_per_candidate_list[2])}% ({str(total_votes_per_candidate_list[2])})\n"
output6 = f"Winner: {winner}\n"
output_list = [output1, output_dash, output2, output_dash, output3, output4, output5, output_dash, output6, output_dash]

# Print the results to the terminal 
for row in output_list:
    print(row)

# Export a text file with the results
# Set var for output file
output_file = os.path.join('analysis', 'election_data_analysis.txt')
#  Open the output file
with open(output_file, "w") as textfile:
     # Write the output rows
    for row in output_list:
        textfile.write(row)
        textfile.write('\n')
# Done writing to the output file

print("\n The Election Results are exported to the text file.\n")