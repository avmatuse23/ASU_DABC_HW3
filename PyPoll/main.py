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
    first_row = next(csvreader)
    print(first_row)
