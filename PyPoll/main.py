#PYPoll

import os

import csv

total_votes = 0

candidates = {}

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open (csvpath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        csv_header = next(csvfile)

        for row in csv_reader:

            total_votes = total_votes + 1
            
            name = row[2]

            if name not in candidates:
                #add the candidate to vote_count
                candidates[name] = 1
            else:
                candidates[name] = candidates[name] + 1



print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for candidate_name, vote_count in candidates.items():
    print(f"{candidate_name}: {vote_count}")  
print("-----------------------")