# Alena Matusevich    10/08/2023
# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
 
import os
import csv

# A set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(budget_data_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    header = next(csvreader)
    print(header)
    # Read the first row to initialies vars
    #first_row = next(csvreader)
    #print(first_row)
    # Set var for the total number of votes cast
    total_votes = 0
    # Set a dicdtionary to hold candidates names and number of votes for each candidate
    candidates_dict = {}
     # Loop through a set of poll data to add the total number of votes each candidate won
    for row in csvreader:
        total_votes += 1
        candidates_dict[row[2]] = 0
    #  Done working with CSV file
    print(f"Total votes: {total_votes}")
    print("Candidates dictionary")
    print(candidates_dict)
    #for key, value in votes_per_candidate.items():
        #print(f"{key}: {value}")
with open(budget_data_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    header = next(csvreader)
    for row in csvreader:
        candidates_dict[row[2]] += 1
    print("Candidates dictionary")
    print(candidates_dict)
