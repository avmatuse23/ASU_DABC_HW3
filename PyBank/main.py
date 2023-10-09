# Alena Matusevich    10/06/2023
# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company.
 
import os
import csv

# Financial dataset called budget_data.csv is composed of two columns: "Date" and "Profit/Losses".
# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    header = next(csvreader)
    # Read the first row to initialies vars
    first_row = next(csvreader)
    # The total number of months included in the dataset is the same as the number of rows
    total_months = 1 # because I read the first row above 
    # The net total amount of "Profit/Losses" over the entire period
    net_profit_losses = float(first_row[1])
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    previous_month_profit_losses = float(first_row[1])
    current_month_profit_losses = 0.0
    mothly_change_in_profits = 0.0 
    net_months_profit_losses = 0.0
    average_months_profit_losses = 0.0
    # The greatest increase in profits (date and amount) over the entire period
    greatest_increase_profit_losses = float(first_row[1])
    date_greatest_increase_profit_losses = first_row[0]
    # The greatest decrease in profits (date and amount) over the entire period
    greatest_decrease_profit_losses = float(first_row[1])
    date_greatest_decrease_profit_losses = first_row[0]
    # Loop through the data to analyzes the records 
    for row in csvreader:
        total_months += 1
        net_profit_losses += float(row[1])
        current_month_profit_losses = float(row[1])
        mothly_change_in_profits = current_month_profit_losses - previous_month_profit_losses
        net_months_profit_losses += mothly_change_in_profits
        previous_month_profit_losses = float(row[1])
        # Check for greates increase
        if mothly_change_in_profits > greatest_increase_profit_losses:
            greatest_increase_profit_losses = mothly_change_in_profits
            date_greatest_increase_profit_losses = row[0]
        # Check for greates decrease
        if mothly_change_in_profits < greatest_decrease_profit_losses:
            greatest_decrease_profit_losses = mothly_change_in_profits
            date_greatest_decrease_profit_losses = row[0]
# Done working with CSV file 

# Calulate average value 
average_months_profit_losses = net_months_profit_losses / (total_months-1)

# Create finantial summary output vars to print and write to the file
output1 = "Financial Analysis"
output2 = "----------------------------"
output3 = f"Total Months: {str(int(total_months))}"
output4 = f"Total: ${str(int(net_profit_losses))}"
output5 = f"Average Change: ${str(round(average_months_profit_losses,2))}"
output6 = f"Greatest Increase in Profits: {date_greatest_increase_profit_losses} (${str(int(greatest_increase_profit_losses))})"
output7 = f"Greatest Decrease in Profits: {date_greatest_decrease_profit_losses} (${str(int(greatest_decrease_profit_losses))})"

#  Print the financial records analysis summary 
print("")
print(output1)
print("")
print(output2)
print("")
print(output3)
print("")
print(output4)
print("")
print(output5)
print("")
print(output6)
print("")
print(output7)
print("")

# Set an output list
output_list = [output1, "", output2, "",output3, "",output4, "",output5, "",output6, "",output7] 
# Set var for output file
output_file = os.path.join('analysis', 'budget_data_analysis.txt')
#  Open the output file
with open(output_file, "w") as textfile:
     # Write the output rows
    for row in output_list:
        textfile.write(row)
        textfile.write('\n')
# Done writing to the output file

print(output2)
print("\n The Financial Analysis are exported to the text file. \n")


