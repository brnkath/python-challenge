# Import dependencies
import os
import csv

# Path to the election_data csv in the Resources folder
poll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Read in the CSV file
with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    # for row in csvreader:

# Print output to terminal
print("Election Results")
print()
print("------------------------------------------")
print()
print()
print()
print("------------------------------------------")
print()
print("------------------------------------------")

# Specify the file to write to
output_path = os.path.join("PyPoll", "Analysis", "voting_analysis.txt")

# Open the file using write mode and set a variable to hold the contents
with open(output_path, "w") as datafile:
    # Write to the txt file
    datafile.write(f"Election Results\n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
    datafile.write("\n")
    datafile.write(f"Total Votes: \n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
    datafile.write("\n")
    datafile.write(f"Charles Casper Stockham: \n")
    datafile.write("\n")
    datafile.write(f"Diana DeGette: \n")
    datafile.write("\n")
    datafile.write(f"Raymon Anthony Doane: \n")
    datafile.write("\n")
    datafile.write(f"Winner: \n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
