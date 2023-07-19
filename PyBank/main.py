# Import dependencies
import os
import csv

# Path to the budget_data csv in the Resources folder
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    header = next(csvreader)

    # Set up variables
    all_months = []
    start_row = next(csvreader)
    previous_row = int(start_row[1])
    profit_losses = []
    profit_loss_change = []
    date_greatest_increase = ""
    greatest_increase = ""
    date_greatest_decrease = ""
    greatest_decrease = ""

    # Loop through rows in budget csv
    for row in csvreader:
        # Add each month to the month list
        all_months.append(row[0])
        # Add each date's profits and losses to profit_loss list
        profit_losses.append(row[1])
        profit_losses = [int(i) for i in profit_losses]
        # Calculate the total of each profit/loss change
        change_total = int(row[1]) - previous_row
        previous_row = int(row[1])
        profit_loss_change.append(change_total)

    # Calculate the total months in the csv
    total_months = len(all_months) + 1

    # Calculate total of profits and losses
    profit_losses = sum(profit_losses) + 1088983

    # Caluclate the average change across all months in the csv
    average_change = sum(profit_loss_change) / len(profit_loss_change)
    average_change = round(average_change, 2)

    # Calculate the greatest increase date and value
    greatest_increase = max(profit_loss_change)
    date_greatest_increase_index = profit_loss_change.index(greatest_increase)
    date_greatest_increase = all_months[date_greatest_increase_index]

    # Calculate the greatest decrease date and value
    greatest_decrease = min(profit_loss_change)
    date_greatest_decrease_index = profit_loss_change.index(greatest_decrease)
    date_greatest_decrease = all_months[date_greatest_decrease_index]

# Print output to the terminal
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})")

# Specify the file to write to
output_path = os.path.join("PyBank", "Analysis", "budget_analysis.txt")

# Open the file using write mode and set a variable to hold the contents
with open(output_path, "w") as datafile:
    # Write to the text file
    datafile.write(f"Financial Analysis\n")
    datafile.write("\n")
    datafile.write("------------------------------------------\n")
    datafile.write("\n")
    datafile.write(f"Total Months: {total_months}\n")
    datafile.write("\n")
    datafile.write(f"Total: ${profit_losses}\n")
    datafile.write("\n")
    datafile.write(f"Average Change: ${average_change}\n")
    datafile.write("\n")
    datafile.write(
        f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\n"
    )
    datafile.write("\n")
    datafile.write(
        f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})\n"
    )
