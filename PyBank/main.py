# Import dependencies
import os
import csv

# Path to the budget_data csv in the Resources folder
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    # for row in csvreader:

# Print output to terminal
print("Financial Analysis")
print("------------------------------------------")
print()
print()
print()
print()
print()

# Specify the file to write to
output_path = os.path.join("PyBank", "Analysis", "budget_analysis.txt")

# Open the file using write mode and set a variable to hold the contents
with open(output_path, "w") as datafile:
    # Write to the txt file
    datafile.write(f"Financial Analysis\n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
    datafile.write("\n")
    datafile.write(f"Total Months: \n")
    datafile.write("\n")
    datafile.write(f"Total: \n")
    datafile.write("\n")
    datafile.write(f"Average Change: \n")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Profits: \n")
    datafile.write("\n")
    datafile.write(f"Greatest Decrease in Profits: \n")
