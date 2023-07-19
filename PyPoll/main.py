# Import dependencies
import os
import csv

# Set up the path to the election_data csv in the Resources folder
poll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")


# Set up a function to create a dictionary with each candidate's name and add a vote count
def votes(candidate_info):
    individual_candidate = candidate_info[2]

    if individual_candidate in candidates:
        candidates[individual_candidate] += 1
    else:
        candidates[individual_candidate] = 1
    return candidates


# Set up a function to calculate the percentage of votes each candidate received
def perc_of_votes():
    perc_of_votes = (candidates[individual_candidate] / total_votes) * 100
    return perc_of_votes


# Read in the CSV file
with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    header = next(csvreader)

    # Set up variables
    total_votes = 0
    candidates = {}
    high_percentage = 0
    winner = ""
    candidate_information = ""

    # Set up a loop to count the total number of votes and add individual candidate information to the candidates dictionary
    for row in csvreader:
        total_votes += 1
        candidates = votes(row)

    # Set up a loop to calculate each candidates percentage of the votes, determine the winner, and add candidate name, percentage, and vote count to the candidate information variable
    for individual_candidate in candidates:
        candidate_percentage = perc_of_votes()
        if candidate_percentage > high_percentage:
            high_percentage = candidate_percentage
            winner = individual_candidate
        candidate_information += f"{individual_candidate}: {candidate_percentage:.3f}% ({candidates[individual_candidate]})\n"

# Print output to the terminal
print(f"Election Results")
print("------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------")
print(f"{candidate_information}")
print("------------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------------")

# Specify the file to write to
output_path = os.path.join("PyPoll", "Analysis", "voting_analysis.txt")

# Open the file using write mode and set a variable to hold the contents
with open(output_path, "w") as datafile:
    # Write to the text file
    datafile.write(f"Election Results\n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
    datafile.write("\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
    datafile.write("\n")
    datafile.write(f"{candidate_information}\n")
    datafile.write("\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
