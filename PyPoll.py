# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import csv
import os

##Method 1 : DIRECT PATH
#  file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()

##Method 2 : INDIRECT PATH
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.

with open(file_to_load, 'r') as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read and print the header row.
    headers = next(file_reader)
    print(headers)

   # Print each row in the CSV file.
    for row in file_reader:
        print(row)
# with open(file_to_save, "w") as txt_file:
#       #To do: perform analysis.
#      print(election_data)

 # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

# # Write three counties to the file.
#      txt_file.write("Counties in the Election\n")
#      txt_file.write("------------\n")
#      txt_file.write("Arapahoe\nDenver\nJefferson")


# Close the file
#outfile.close()