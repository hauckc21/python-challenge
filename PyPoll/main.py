import os

import csv

#Define variables
total_votes = 0
candidates = {}

#Store csv file path
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#Open csv in read mode
with open (csvpath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        #Read the header row
        csv_header = next(csvfile)

        #Read through each row of data after the header
        for row in csv_reader:

            #Count total votes
            total_votes = total_votes + 1
            
            #search for name in dataset
            name = row[2]

            if name not in candidates:
                #add the candidate to candidates dictionary
                candidates[name] = 1

            #Move and and find next candidates name    
            else:
                candidates[name] = candidates[name] + 1


#Print results to terminal
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for candidate_name, vote_count in candidates.items():
    percentage = round((vote_count / total_votes * 100), 3) 
    print(f"{candidate_name}: {percentage}% ({vote_count})")     
print("-----------------------")

winner = sorted(candidates.items(), reverse=False)
print("Winner:" + str(winner[1][0]))
print("-----------------------")

#Export text file with results
election_analysis = os.path.join("Analysis", "election_analysis.txt")
with open(election_analysis, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-----------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-----------------------\n")
    for candidate_name, vote_count in candidates.items():
        percentage = round((vote_count / total_votes * 100), 3)
        outfile.write(f"{candidate_name}: {percentage}% ({vote_count})\n")   
    outfile.write("-----------------------\n")
    
    winner = sorted(candidates.items(), reverse=False)
    outfile.write("Winner:" + str(winner[1][0]))
    outfile.write("                        \n")
    outfile.write("-----------------------\n")